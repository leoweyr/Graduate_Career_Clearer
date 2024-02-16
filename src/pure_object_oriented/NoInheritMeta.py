from typing import Type, List


class NoInheritMeta(type):
    is_inherited: bool = False

    def __new__(mcs: Type['NoInheritMeta'], class_name: str, base_classes: tuple,
                attributes_and_methods: dict) -> 'NoInheritMeta':
        if len(base_classes) > 0:
            non_inherited_class_names_list: List[str] = []

            for base_class in base_classes:
                if hasattr(base_class, "is_inherited") and base_class.is_inherited is False:
                    non_inherited_class_names_list.append(base_class.__name__)

            if len(non_inherited_class_names_list) > 0:
                non_inherited_class_names: str = ', '.join(non_inherited_class_names_list)
                raise TypeError(f"Class <{class_name}> cannot inherit from class <{non_inherited_class_names}>")

        return super().__new__(mcs, class_name, base_classes, attributes_and_methods)
