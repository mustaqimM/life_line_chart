from life_line_chart import AncestorGraph, get_gedcom_instance_container
import os

def test_generate_svg_file():
    max_generations = 20
    x_position = 0

    # select individual to show
    gedcom_data = open(os.path.join(os.path.dirname(__file__), 'autogenerated.ged'),'r').read()
    last_individual_pos = gedcom_data.rfind('\n0 @I')
    last_individual_pos = gedcom_data.rfind(' FAMC ', 0, last_individual_pos)
    last_individual_pos = gedcom_data.rfind('\n0 @I', 0, last_individual_pos)
    individual_id = gedcom_data[last_individual_pos+3:gedcom_data.find(' INDI',last_individual_pos+1)]

    graph = AncestorGraph(instance_container=lambda : get_gedcom_instance_container(os.path.join(os.path.dirname(__file__), 'autogenerated.ged')))
    graph.select_individuals(graph._instances[('i', individual_id)], generations = max_generations)

    cof_ids = graph._instances[('i',individual_id)].child_of_family_id
    child_of_family = None
    if cof_ids:
        child_of_family = graph._instances[('f',cof_ids[0])]
    graph.place_selected_individuals(graph._instances[('i',individual_id)], None, None, child_of_family, x_position)
    width = graph._instances[('i',individual_id)].graphical_representations[0].get_width(None)
    x_position += width

    graph.modify_layout(individual_id)

    graph.define_svg_items()
    graph.paint_and_save(individual_id, os.path.join(os.path.dirname(__file__), 'output', 'test_svg.svg'))

def test_generate_svg_file_with_two_roots():
    max_generations = 20
    x_position = 0
    last_individual_pos = None
    graph = AncestorGraph(instance_container=lambda : get_gedcom_instance_container(os.path.join(os.path.dirname(__file__), 'autogenerated.ged')))
    
    # select individual to show
    gedcom_data = open(os.path.join(os.path.dirname(__file__), 'autogenerated.ged'),'r').read()
    last_individual_pos = gedcom_data.rfind(' FAMC ', 0, last_individual_pos)
    last_individual_pos = gedcom_data.rfind('\n0 @I', 0, last_individual_pos)
    individual_id = gedcom_data[last_individual_pos+3:gedcom_data.find(' INDI',last_individual_pos+1)]

    graph.select_individuals(graph._instances[('i', individual_id)], generations = max_generations)

    cof_ids = graph._instances[('i',individual_id)].child_of_family_id
    child_of_family = None
    if cof_ids:
        child_of_family = graph._instances[('f',cof_ids[0])]
    graph.place_selected_individuals(graph._instances[('i',individual_id)], None, None, child_of_family, x_position)
    width = graph._instances[('i',individual_id)].graphical_representations[0].get_width(None)
    x_position += width
    graph.modify_layout(individual_id)

    # select individual to show
    #gedcom_data = open(os.path.join(os.path.dirname(__file__), 'autogenerated.ged'),'r').read()
    last_individual_pos = gedcom_data.rfind(' FAMC ', 0, last_individual_pos-int(len(gedcom_data)*0.2))
    last_individual_pos = gedcom_data.rfind(' FAMC ', 0, last_individual_pos)
    last_individual_pos = gedcom_data.rfind('\n0 @I', 0, last_individual_pos)
    individual_id = gedcom_data[last_individual_pos+3:gedcom_data.find(' INDI',last_individual_pos+1)]

    graph.select_individuals(graph._instances[('i', individual_id)], generations = max_generations)

    cof_ids = graph._instances[('i',individual_id)].child_of_family_id
    child_of_family = None
    if cof_ids:
        child_of_family = graph._instances[('f',cof_ids[0])]
    graph.place_selected_individuals(graph._instances[('i',individual_id)], None, None, child_of_family, x_position)
    width = graph._instances[('i',individual_id)].graphical_representations[0].get_width(None)
    x_position += width
    try:
        #graph.modify_layout(individual_id) änot working yet for multiple root individuals
        pass
    except:
        pass

    graph.define_svg_items()
    graph.paint_and_save(individual_id, os.path.join(os.path.dirname(__file__), 'output', 'test_svg_two_roots.svg'))

