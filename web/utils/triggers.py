import pgtrigger

__all__ = ("ProtectColumn",)


class ProtectColumn(pgtrigger.Trigger):
    """A trigger which raises an exception when a specific column is updated."""

    operation = pgtrigger.Update
    when = pgtrigger.Before

    def __init__(self, *, name: str, column: str, name_column: str = "name"):
        condition = ~pgtrigger.Q(**{f"new__{column}": pgtrigger.F(f"old__{column}")})
        super().__init__(name=name, condition=condition)

        self.column = column
        self.name_column = name_column

    def get_func(self, model):
        return f"""
        RAISE EXCEPTION 'Cannot update % ''%'': updating column ''{self.column}'' is disallowed',
            TG_TABLE_NAME, OLD.{self.name_column};
        """
