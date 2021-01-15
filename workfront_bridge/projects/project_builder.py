class ProjectBuilder(object):
    def register_field(self, field_name, default_value=None):
        def setter(value):
            setattr(self, field_name, value)
            return self
        setter_name = "set_{}".format(field_name)

        setattr(self, field_name, default_value)
        setattr(self, setter_name, setter)
