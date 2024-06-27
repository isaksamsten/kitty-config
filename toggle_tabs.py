from kittens.tui.handler import result_handler
from kitty.fast_data_types import get_options


def main():
    pass


@result_handler(no_ui=True)
def handle_result(args, result, target_window_id, boss):
    # Get the old tab bar style
    opts = get_options()
    if opts.tab_bar_style == "separator":
        tab_bar_style = "hidden"
    else:
        tab_bar_style = "separator"

    # Save the layout of all tabs.
    layout = [t.current_layout.name for t in boss.all_tabs]

    # Override the tab_bar_style
    boss.load_config_file(
        *(),
        apply_overrides=True,
        overrides=("tab_bar_style %s" % tab_bar_style,),
    )

    # Restore the layouts
    for t, layout in zip(boss.all_tabs, layout):
        t.goto_layout(layout)
