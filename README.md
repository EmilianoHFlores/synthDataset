# synthDataset
Either the heavy or light model of segment-anything needs to be downloades.
```console
$ wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
```
Workflow to obtain a dataset:

- Use autoCut.py to obtain all cut objects from a folder with images. Inside the script, change the folder and the object to look for.
- Use cutPng.py to crop objects to its minimum size.
- Use create_dataset to generate both the image sets and the annotations in COCO format.
