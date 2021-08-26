from django.db.models import Q

from caluma.caluma_core.types import Node
from caluma.caluma_core.visibilities import BaseVisibility, Union, filter_queryset_for
from caluma.caluma_form.schema import Answer, Document, Form, Option, Question
from caluma.caluma_workflow.schema import Flow, Task, Workflow, WorkItem


class StaffVisibility(BaseVisibility):
    @filter_queryset_for(Node)
    def filter_queryset_for_all(self, node, queryset, info):
        user = info.context.user
        if "sagw" in user.groups or "admin" in user.groups:
            return queryset

        return queryset.none()


class CreateOrAssignVisibility(BaseVisibility):
    @filter_queryset_for(Node)
    def filter_queryset_for_all(self, node, queryset, info):
        user = info.context.user
        return queryset.filter(created_by_user=user.username)

    @filter_queryset_for(Answer)
    def filter_queryset_for_answer(self, node, queryset, info):
        user = info.context.user
        return queryset.filter(
            Q(created_by_user=user.username)
            | Q(document__created_by_user=user.username)
        )

    @filter_queryset_for(Document)
    def filter_queryset_for_document(self, node, queryset, info):
        user = info.context.user
        return queryset.filter(
            Q(created_by_user=user.username)
            | Q(work_item__assigned_users__contains=[user.username])
        )

    @filter_queryset_for(WorkItem)
    def filter_queryset_for_workitem(self, node, queryset, info):
        user = info.context.user
        return queryset.filter(
            Q(assigned_users__contains=[user.username])
            | Q(addressed_groups__contains=[user.group])
        )

    @filter_queryset_for(Task)
    @filter_queryset_for(Flow)
    @filter_queryset_for(Workflow)
    @filter_queryset_for(Form)
    @filter_queryset_for(Option)
    @filter_queryset_for(Question)
    def filter_queryset_for_blueprints(self, node, queryset, info):
        return queryset


class MySAGWVisibility(Union):
    visibility_classes = [StaffVisibility, CreateOrAssignVisibility]
