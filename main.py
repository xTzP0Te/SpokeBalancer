import flet as ft
import yaml


def main(page: ft.Page):

    def dd_tools_changed(e):
        print(dd_tools.value)
        dd_spokes.options.clear()
        options_list = list()
        for spoke_key in spoke_tension_tables[dd_tools.value].keys():
            options_list.append(ft.dropdown.Option(spoke_key))
            # dd_spokes.options.append(ft.dropdown.Option(spoke_key))
        dd_spokes.options = options_list
        print(options_list)
        dd_spokes.visible = True
        page.update()
        page.add(dd_spokes)

    def dd_spokes_changed(e):
        tension_values = spoke_tension_tables[dd_tools.value][dd_spokes.value]['Tension']
        readings_values = spoke_tension_tables[dd_tools.value][dd_spokes.value]['Readings']

        column_list = [ft.DataColumn(ft.Text(""))]
        row_tension = [ft.DataCell(ft.Text("Натяжение"))]
        row_readings = [ft.DataCell(ft.Text("Значение"))]

        for col in range(len(tension_values)):
            column_list.append(ft.DataColumn(ft.Text(""), numeric=True))
            row_tension.append(ft.DataCell(ft.Text(tension_values[col])))
            row_readings.append(ft.DataCell(ft.Text(readings_values[col])))

        table_readings.visible = True
        table_readings.columns = column_list
        table_readings.rows = [ft.DataRow(cells=row_tension), ft.DataRow(cells=row_readings)]
        # table_readings = ft.DataTable(
        #     columns=column_list,
        #     rows=[
        #         ft.DataRow(
        #             cells=row_tension
        #         ),
        #         ft.DataRow(
        #             cells=row_readings
        #         )
        #     ]
        # )
        page.update()
        # table_readings.update()e

        print(tension_values)
        print(readings_values)

    dd_tools = ft.Dropdown(
        on_change=dd_tools_changed,
        autofocus=True,
        border_radius=ft.border_radius.all(10),
        # padding=ft.padding.only(left=10),
        elevation=10,
        label="Инструмент",
        width=max(len(str(s)) for s in tools_list) * 10,
        options=tools_list,
    )
    page.add(dd_tools)

    # spokes_list = list()
    dd_spokes = ft.Dropdown(
        on_change=dd_spokes_changed,
        visible=False,
        autofocus=True,
        border_radius=10,
        elevation=10,
        label="Спицы",
        width=300,
        options=[],
    )
    page.add(dd_spokes)

    table_readings = ft.DataTable(
        visible=False,
        columns=[ft.DataColumn(ft.Text(""))],
        rows=[
            ft.DataRow(
                cells=[ft.DataCell(ft.Text(""))]
            )
        ]
    )
    page.add(table_readings, ft.Divider())


if __name__ == '__main__':
    # Открываем и читаем YAML файл
    with open('spoke_tension_tables.yaml', 'r') as file:
        spoke_tension_tables = yaml.safe_load(file)

    tools_list = list()
    for key in spoke_tension_tables.keys():
        tools_list.append(ft.dropdown.Option(key))

    ft.app(target=main)
