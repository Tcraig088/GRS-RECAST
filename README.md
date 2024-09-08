Two Folders are available in this repository. 

Launcher - 
  This contains python scripts to be used with RECAST3D and Slicerecon binaries.
  The scripts contain
    - Preprocess alignments
    - Gui for setting reconstruction and alignment parameters
    - code for importing images
    - Multiprocess code for passing arguments between the gui and the plugin/alignments
    
  Must be run on linux - includes binaries for recast3d and slicerecon however these can be built from source at 
  https://github.com/cicwi/RECAST3D
  
  BeamSimulator
    This contains matlab code for simulating beam damage and a tutorial script titled tutorial.m
    should be used with astra and tomohawk which are included in a subdirecotry
