import os

def replace_label(root_dir, old_label="0", new_label="4"):
    """
    批量修改 YOLO 格式标签（仅替换每行的第一个数字）
    root_dir : str，目标目录的绝对路径
    old_label : str，要替换的原标签
    new_label : str，新标签
    """
    if not os.path.isdir(root_dir):
        print(f"❌ 目录不存在：{root_dir}")
        return

    txt_files = [f for f in os.listdir(root_dir) if f.endswith(".txt")]

    if not txt_files:
        print("⚠️ 该目录下没有 .txt 文件")
        return

    for file in txt_files:
        txt_path = os.path.join(root_dir, file)
        new_lines = []

        with open(txt_path, "r") as f:
            for line in f:
                parts = line.strip().split()

                # 若不是合法 YOLO 行则跳过
                if len(parts) < 5:
                    new_lines.append(line)
                    continue

                # 替换标签
                if parts[0] == old_label:
                    parts[0] = new_label

                new_lines.append(" ".join(parts) + "\n")

        # 写回文件
        with open(txt_path, "w") as f:
            f.writelines(new_lines)

        print(f"✔ 已处理：{txt_path}")

    print("\n🎉 全部 txt 文件标签修改完成！")


if __name__ == "__main__":
    # 示例：你可以修改成你的目录路径
    directory = "/home/junfaimec/object_detection/dataset/Inner-Mongolia-cattle-Behaviour/CMBD/l"
    replace_label(directory, old_label="0", new_label="4")
