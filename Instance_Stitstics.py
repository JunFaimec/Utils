import os
from collections import defaultdict

def count_yolo_instances(labels_dir: str):
    """
    统计 YOLO 标签目录下每一类的实例数量
    :param labels_dir: 绝对路径，指向 YOLO 的 labels/ 目录或包含 .txt 的目录
    """
    if not os.path.isdir(labels_dir):
        print(f"路径不存在: {labels_dir}")
        return

    class_count = defaultdict(int)

    # 遍历目录下所有 .txt 标签文件
    for root, _, files in os.walk(labels_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    for line in f.readlines():
                        line = line.strip()
                        if not line:
                            continue
                        parts = line.split()
                        class_id = parts[0]   # YOLO 标签格式：class x y w h ...
                        class_count[class_id] += 1

    # 输出统计结果
    print("\n=== YOLO 类别实例统计结果 ===")
    if not class_count:
        print("未找到任何 YOLO 标签文件或无有效内容。")
        return

    for cls in sorted(class_count, key=lambda x: int(x)):
        print(f"类别 {cls}: {class_count[cls]} 个实例")


if __name__ == "__main__":
    path = ' '
    count_yolo_instances(path)
