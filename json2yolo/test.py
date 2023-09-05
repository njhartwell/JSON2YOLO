import general_json2yolo
import sys

if __name__ == '__main__':
    general_json2yolo.convert_coco_json(sys.argv[1], use_segments=True, cls91to80=False)