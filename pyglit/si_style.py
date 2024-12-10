from plotnine import *

def si_style(
    font_title="Arial",
    font_subtitle="Arial",
    font_plot="Arial",
    font_caption="Arial",
    facet_space=2,
    text_scale=1,
    FO=False,
    **kwargs
):
    """
    This function adorns your plotnine plot to convert it into SI style.
    """

    # Set default colors
    COLOR_PLOT_TEXT = "#000000" if FO else "#505050"
    COLOR_TITLE = "#000000" if FO else "#202020"
    COLOR_CAPTION = "#000000" if FO else "#909090"
    COLOR_GRIDLINE = "#D3D3D3"

    HALF_LINE = 5.5

    return (
        theme_minimal()
        + theme(
            # Title and subtitle
            plot_title=element_text(
                family=font_title,
                size=14 * text_scale,
                weight="bold",
                color=COLOR_TITLE,
                margin={"b": HALF_LINE},
                ha="left",
            ),
            plot_subtitle=element_text(
                family=font_subtitle,
                size=12 * text_scale,
                color=COLOR_TITLE,
                margin={"b": HALF_LINE},
                ha="left",
            ),
            plot_caption=element_text(
                family=font_caption,
                size=9 * text_scale,
                color=COLOR_CAPTION,
                margin={"t": HALF_LINE / 2},
                ha="right",
            ),
            plot_margin_top=.03,
            plot_margin_bottom=.02,
            plot_margin_left=.03,
            plot_margin_right=.03,
            
            # Legend settings
            legend_direction='horizontal',
            legend_position='top',
            legend_justification = (0,0),
            legend_text=element_text(family=font_plot, 
                                     size=11 * text_scale, 
                                     color=COLOR_PLOT_TEXT),
            legend_title=element_text(family=font_plot, 
                                      size=11 * text_scale, 
                                      color=COLOR_PLOT_TEXT),
            legend_key=element_blank(),

            # Axis settings
            axis_text=element_text(family=font_plot, 
                                   size=10 * text_scale, 
                                   color=COLOR_PLOT_TEXT),
            axis_ticks=element_blank(),
            axis_title=element_text(family=font_plot, 
                                    size=10 * text_scale, 
                                    color=COLOR_PLOT_TEXT),

            # Grid lines
            panel_grid_minor=element_blank(),
            panel_grid_major_y=element_line(color = COLOR_GRIDLINE, 
                                            linewidth = 0.25),
            panel_grid_major_x=element_line(color = COLOR_GRIDLINE, 
                                            linewidth = 0.25),

            #Blank background
            panel_background = element_blank(),
            panel_border = element_blank(),
            panel_spacing = facet_space,

            # Plot fill and margins
            plot_background = element_rect(fill = "white", color = None),

            #Strip background (This sets the panel background for facet-wrapped plots to white)
            strip_background = element_blank(),
            strip_text = element_text(
                family = font_title,
                size  = 11 * text_scale,
                ha = "center",
                color = COLOR_PLOT_TEXT,
                margin={"b": HALF_LINE*0.6, "t":HALF_LINE*0.6}
            )                              
        )
    )


