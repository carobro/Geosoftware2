# gehört nicht in den similarity ornder sondern:
# zenodo/config.py
recid_similar=dict(
        pid_type='recid',
        route='/record/<pid_value>/similar',
        template='zenodo_records/record_similar.html',
        view_imp='zenodo.modules.similarity.ui.similar_records',
        record_class='zenodo.modules.records.api:ZenodoRecord',
    ),
)