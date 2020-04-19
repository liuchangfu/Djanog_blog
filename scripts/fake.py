# _*_ coding:utf-8 _*_
import os
import pathlib
import random
import sys
from datetime import timedelta
import django
import faker
from django.utils import timezone
from loguru import logger

back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
logger.info(f'{BASE_DIR}')
sys.path.append(BASE_DIR)

dir = pathlib.PurePath(BASE_DIR).joinpath('scripts', 'md.sample')
logger.info(dir)

# fake = faker.Factory().create('zh_CN')

# for i in range(5):
#     logger.info(f'电话:{i}--{fake.phone_number()}')
#     logger.info(f'姓名：{i}--{fake.name()}')
#     logger.info(fake.address())
#     logger.info(fake.country())
#     logger.info(fake.city_name())
#     logger.info(fake.license_plate())
#     logger.info(fake.paragraphs(10))
#
#

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djanog_blog.settings.local")
    django.setup()
    from blog.models import Category, Post, Tag
    from comments.models import Comment
    from django.contrib.auth.models import User

    logger.info('clean database')
    Post.objects.all().delete()
    Category.objects.all().delete()
    Tag.objects.all().delete()
    Comment.objects.all().delete()
    User.objects.all().delete()

    logger.info('create a blog user')
    user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
    category_list = ['Python学习笔记', '开源项目', '工具资源', '程序员生活感悟', 'test category']
    tag_list = ['django', 'Python', 'Pipenv', 'Nginx', 'Docker', 'Elasticserarch', 'Gunicorn', 'Supervisor', 'test tag']
    a_year_ago = timezone.now() - timedelta(days=365)
    logger.info('create category and tags')
    for cate in category_list:
        Category.objects.create(name=cate)

    for tag in tag_list:
        Tag.objects.create(name=tag)

    logger.info('create a markdown sample post')
    Post.objects.create(
        title='Markdown与代码高亮测试',
        body=pathlib.Path(BASE_DIR).joinpath('scripts', 'md.sample').read_text(encoding='utf-8'),
        category=Category.objects.create(name='Markdown测试'),
        author=user,
    )

    logger.info('create some faked posts published within the past year')
    fake = faker.Faker()  # English
    for _ in range(20):
        tags = Tag.objects.order_by('?')
        tag1 = tags.first()
        tag2 = tags.last()
        cate = Category.objects.order_by('?').first()
        created_time = fake.date_time_between(start_date='-1y', end_date="now",
                                              tzinfo=timezone.get_current_timezone())
        post = Post.objects.create(
            title=fake.sentence().rstrip('.'),
            body='\n\n'.join(fake.paragraphs(10)),
            created_time=created_time,
            category=cate,
            author=user,
        )
        post.tags.add(tag1, tag2)
        post.save()

        fake = faker.Faker('zh_CN')
        for _ in range(20):  # Chinese
            tags = Tag.objects.order_by('?')
            tag1 = tags.first()
            tag2 = tags.last()
            cate = Category.objects.order_by('?').first()
            created_time = fake.date_time_between(start_date='-1y', end_date="now",
                                                  tzinfo=timezone.get_current_timezone())
            post = Post.objects.create(
                title=fake.sentence().rstrip('.'),
                body='\n\n'.join(fake.paragraphs(10)),
                created_time=created_time,
                category=cate,
                author=user,
            )
            post.tags.add(tag1, tag2)
            post.save()

        logger.info('create some comments')
        for post in Post.objects.all()[:20]:
            post_created_time = post.created_time
            delta_in_days = '-' + str((timezone.now() - post_created_time).days) + 'd'
            for _ in range(random.randrange(3, 15)):
                Comment.objects.create(
                    name=fake.name(),
                    email=fake.email(),
                    url=fake.uri(),
                    text=fake.paragraph(),
                    created_time=fake.date_time_between(
                        start_date=delta_in_days,
                        end_date="now",
                        tzinfo=timezone.get_current_timezone()),
                    post=post,
                )

        logger.info('done!')
