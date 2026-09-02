{# Availability badges for Berlin 2025.
   Variables (set via `{% with %}` before include):
     in_person : bool   - Available to in-person attendees
     virtual   : bool   - Available to virtual attendees
     note      : string - Optional short clarifier (e.g. "live streamed", "separate track")
#}
<p class="availability">
{% if in_person %}<span class="availability-badge availability-in-person" title="Available to in-person attendees">📍 In person</span>{% endif %}
{% if virtual %}<span class="availability-badge availability-virtual" title="Available to virtual attendees">💻 Virtual</span>{% endif %}
{% if note %}<span class="availability-note">{{ note }}</span>{% endif %}
</p>
