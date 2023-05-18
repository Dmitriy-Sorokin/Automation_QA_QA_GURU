def resource(relative_path):
    import page_objct_final.demoqa_tests
    from pathlib import Path
    return (
        Path(page_objct_final.demoqa_tests.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )
