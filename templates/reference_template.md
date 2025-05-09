{{test_name}}


# Annotations
{% for annotation in itemAnnotations %}


{{annotation.color}}
{% if annotation.text %}{{annotation.text}}{% endif %}
{% if annotation.pagelabel%} {{annotation.pagelabel}}{% endif %}
{% if annotation.comment %}
> {{annotation.comment}}
{% endif %}


{% endfor %}

# Notes
{% for note in itemNotes %}
{{note.note}} 
{% endfor %}
