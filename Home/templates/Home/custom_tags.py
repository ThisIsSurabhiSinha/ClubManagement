from django import template

register = template.Library()
@register.filter
def get_user_group(user):
    # Check if the user is in any of the specified groups
    all_groups = Group.objects.all()
    user_groups = user.groups.all()

    for group in all_groups:
        if group in user_groups:
            return group.name
    return None