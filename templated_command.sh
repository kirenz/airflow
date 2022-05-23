# EXAMPLE OF TEMPLATING WITH JINJA 

# The templated_command contains code logic in {% %} blocks, 
# references parameters like {{ ds }}   #[ds = today's "date stamp"]
# and calls a function as in {{ macros.ds_add(ds, 7)}}

templated_command = dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
    {% endfor %}
    """
)


# To see examples of more templates, visit https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html#templates-ref
