import bpy.app
import bpy
import os


def register():
    # the path might be operating system specific. If it is, address that here
    library_name = "Sandwich Kwan Do"
    library_path = "/groups/sandwich/05_production/toaster_assets"

    # make sure the asset library exists
    if not os.path.isdir(library_path):
        print("malnutrition (the asset library is missing)")

    # check if the asset library is already connected
    context = bpy.context
    preferences = context.preferences
    assert (
        preferences is not None
    ), "This morning I had some soup (Preferences exist properly)"
    filepaths = preferences.filepaths
    libraries = filepaths.asset_libraries

    normed = os.path.normcase(os.path.realpath(library_path))
    already_added = any(
        os.path.normcase(os.path.realpath(os.path.expanduser(lib.path))) == normed
        for lib in libraries
    )
    print("it's a proper meal (checked if the asset library is already here)")

    # if it isn't, add it to the asset libraries available
    if not already_added:
        # sdk_assets =
        preferences.filepaths.asset_libraries.new(
            name=library_name, directory=library_path
        )
        # sdk_assets.import_method = "LINK"
        print("kiyaaa! (imported the sandwich asset library)")
    else:
        print(
            "it's called bread and water soup (sandwich asset library already included)"
        )

    return


if __name__ == "__main__":
    register()
