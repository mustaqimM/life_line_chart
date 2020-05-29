
class GraphicalFamily():
    """
    Class which represents one appearance of a family
    """
    _x_position = None
    # color = 'rgb(200,200,255)'

    def __init__(self, instances, family_id):
        self.graphical_representations = []
        self.family_id = family_id
        self.__instances = instances
        self.family = self.__instances[('f', self.family_id)]
        self.family.graphical_representations.append(self)
        self.marriage = self.family.marriage

        # Tells which children are visible
        self.visible_children = []

        # Descendant chart: Used to define under which family this family has
        # been placed (e.g. if wife/husband are from different branches of the
        # family)
        self.visual_placement_parent_family = None
        self.children_width = None
        self.g_id = None

    def __repr__(self):
        return 'gr_family "' + self.family.husb_name + '"+"' + self.family.wife_name + '"'

    def get_spouse(self, individual):
        spouse = self.family.get_spouse(
            individual.individual_id)
        if not spouse or not spouse.graphical_representations:
            return None
        return self.family.get_spouse(individual.individual_id).graphical_representations[0]

    def add_visible_children(self, gr_individual):
        if gr_individual not in self.visible_children and gr_individual.birth_date_ov:
            self.visible_children.append(gr_individual)
            self.visible_children.sort()
            # (
            #     gr_individual.birth_date_ov,
            #     len(self.visible_children),
            #     gr_individual
            # )

    @property
    def husb_name(self):
        return self.family.husb_name

    @property
    def wife_name(self):
        return self.family.wife_name

    @property
    def husb(self):
        return self.family.husb

    @property
    def wife(self):
        return self.family.wife

    @property
    def marriage_label(self):
        return self.family.marriage_label

