import os

def make_temp_dir(infile):
    """
    Make sure that the temp directory, '.cache' exists and if not is created
    The infile parameter should contain the path to the calling file.  if you call this from your program thus

    my_var = make_temp_dir(__file__)

    it will always work
    """

    script_dir = os.path.dirname(infile)
    cache_dir = os.path.join(script_dir, ".cache")
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)

    return cache_dir


if __name__== "__main__":
    print(f"{make_temp_dir(__file__)}")
