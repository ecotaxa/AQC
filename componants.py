from dash import dcc
from dash import html
from dash.dependencies import Input, Output

def generate_header():
    return html.Div([
                    html.H1('Data quality checks'),
                    html.Span(className='elementor-divider-separator')
                ],
                className="container-header")

def generate_project_selector(drives):
    return html.Div([
        html.H2("Drive"),
        dcc.Dropdown(
            id='app-1-dropdown-drives',
            value= "zooscan_embrc",
            options=[
                {'label': drive.name, 'value': drive.name} for drive in drives
            ]
        ),
        html.H2("Project"),
        dcc.Dropdown(
            id='app-1-dropdown-projects',
            value=drives[0].name,
            multi=True
        )
    ], className="container-prj-selector")

def generate_check_block(checkBlock) :
    return html.Div([  ##-- check list title --###
                    html.Div([
                                dcc.Checklist(
                                    options=[{'label': checkBlock["title"], 'value': checkBlock["id"]}],
                                    labelStyle={'display': 'block'},
                                    className="h3 inline"
                                ),
                                html.Img(className="runQC-btn",src="../assets/play.png", alt="Run selected QC")
                            ],
                            className="check-block-title"),
                    ###-- check list tab --###   
                    html.Div([
                        dcc.Tabs(
                            id="tabs-"+checkBlock["id"],
                            value='tab-'+checkBlock["id"],
                            parent_className='custom-tabs',
                            className='custom-tabs-container',
                            children=[
                                dcc.Tab(
                                    label='Details',
                                    value='tab-details-'+checkBlock["id"],
                                    className='custom-tab',
                                    selected_className='custom-tab--selected'
                                ),
                                dcc.Tab(
                                    label='Results',
                                    value='tab-result-'+checkBlock["id"],
                                    className='custom-tab',
                                    selected_className='custom-tab--selected'
                                )
                            ]
                        ),
                        html.Div(id='tabs-content-'+checkBlock["id"])
                    ])  
                ]) 

def generate_checks_block(checks):
    checks_layout=[]
    for check in checks :
        checks_layout.append(
            html.Div([
                html.H5(check["title"]),
                html.P(check["description"])
            ])
        )
    return html.Div(checks_layout,className="checks-block")

    
def generate_sub_block(sub_block) : 
    return html.Div([
        html.H3(sub_block["title"]),
        html.P(sub_block["description"]),
        generate_checks_block(sub_block["checks"]),
    ],className="sub-block")


def generate_details(checkBlock):
    sub_blocks = []
    for sub_block in checkBlock["blocks"] :
        sub_blocks.append(generate_sub_block(sub_block))
    return html.Div(sub_blocks,className="tab-div-common details")

def generate_result(checkBlock):
    return html.Div([
        html.P('Tab content result'+checkBlock["id"])
    ], className="tab-div-common")

