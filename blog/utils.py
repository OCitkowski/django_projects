from blog.models import Post, Tag, Category
from django.contrib.auth.mixins import LoginRequiredMixin



menu = [{'title': "Home", 'url_name': ''},
        {'title': "Blog", 'url_name': 'blogs'},
        {'title': "About", 'url_name': 'about'},
        {'title': "Contact", 'url_name': 'contact'},
]

class MixinView():
        model = Post
        paginate_by = 3
        context_object_name = 'posts'



        def get_user_context(self, **kwargs):

                context = kwargs

                context['blog_cats'] = Category.objects.all()
                context['blog_tags'] = Tag.objects.all()
                context['menu'] = menu
                first_posts = Post.objects.filter(status='p').order_by('-date_update')[:2]
                context['first_posts'] = first_posts

                return context
