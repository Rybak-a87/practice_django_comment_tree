def get_children(qs_child):    # формирует информацию о дочерних комментариях
    res = []
    for comment in qs_child:
        com_dict = {
            "id": comment.id,
            "text": comment.text,
            "timestamp": comment.timestamp.strftime("%d-%m-%Y %H:%M"),
            "author": comment.user,
            "is_child": comment.is_child,
            "parent_id": comment.get_parent
        }
        if comment.comment_children.exists():
            com_dict["children"] = get_children(comment.comment_children.all())
        res.append(com_dict)
    return res


def create_comments_tree(qs):    # принимает QuerySet (формирует информацию о комментариях)
    res = []
    for comment in qs:
        com_dict = {
            "id": comment.id,
            "text": comment.text,
            "timestamp": comment.timestamp.strftime("%d-%m-%Y %H:%M"),
            "author": comment.user,
            "is_child": comment.is_child,
            "parent_id": comment.get_parent
        }
        if comment.comment_children:    # проверка, есть ли у комментария дочерние комментарии (comment-children - это related_name из моделей)
            com_dict["children"] = get_children(comment.comment_children.all())
        if not comment.is_child:
            res.append(com_dict)
    return res
