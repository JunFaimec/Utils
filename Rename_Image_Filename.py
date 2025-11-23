import os
import glob
import shutil


def backup_and_rename(image_dir, label_dir):
    """
    将 images 和 labels 目录备份为 *_old  
    然后创建新的 images 和 labels 目录  
    将原文件按顺序复制到新目录并重命名（成对 jpg/txt）
    """

    # 新旧路径
    image_old = image_dir + "_old"
    label_old = label_dir + "_old"

    # ------------ 1. 检查目录 ------------
    if not os.path.exists(image_dir):
        print(f"❌ 图片目录不存在: {image_dir}")
        return
    if not os.path.exists(label_dir):
        print(f"❌ 标签目录不存在: {label_dir}")
        return

    # ------------ 2. 创建备份 ------------
    if not os.path.exists(image_old):
        shutil.move(image_dir, image_old)
        print(f"📦 已备份目录: {image_dir} → {image_old}")
    else:
        print(f"⚠️ 备份目录已存在: {image_old}，跳过移动")

    if not os.path.exists(label_old):
        shutil.move(label_dir, label_old)
        print(f"📦 已备份目录: {label_dir} → {label_old}")
    else:
        print(f"⚠️ 备份目录已存在: {label_old}，跳过移动")

    # ------------ 3. 创建新的空目录 ------------
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(label_dir, exist_ok=True)
    print(f"📂 已创建新目录: {image_dir}, {label_dir}")

    # ------------ 4. 加载旧目录 jpg 文件 ------------
    image_files = sorted(glob.glob(os.path.join(image_old, "*.jpg")))
    if not image_files:
        print("⚠️ 在 images_old 下未找到 jpg 文件")
        return

    # ------------ 5. 开始按顺序复制并重命名 ------------
    idx = 1
    for img_path in image_files:
        img_name = os.path.basename(img_path)
        stem = os.path.splitext(img_name)[0]

        label_path = os.path.join(label_old, f"{stem}.txt")
        if not os.path.exists(label_path):
            print(f"⚠️ 无标签文件，跳过：{img_name}")
            continue

        new_img_path = os.path.join(image_dir, f"{idx}.jpg")
        new_label_path = os.path.join(label_dir, f"{idx}.txt")

        # 复制而不是移动
        shutil.copy(img_path, new_img_path)
        shutil.copy(label_path, new_label_path)

        print(f"✔ 复制重命名: {img_name} → {idx}.jpg   |   {stem}.txt → {idx}.txt")

        idx += 1

    print("\n🎉 全部完成！")
    print(f"新目录中共生成 {idx-1} 对文件。")
    print("原始文件完整保存在 *_old 中。")


if __name__ == "__main__":
    IMAGE_DIR = "/home/junfaimec/object_detection/dataset/Inner-Mongolia-cattle-Behaviour/CMBD/images/val"
    LABEL_DIR = "/home/junfaimec/object_detection/dataset/Inner-Mongolia-cattle-Behaviour/CMBD/labels/val"

    print("🚀 开始备份并重命名...")
    backup_and_rename(IMAGE_DIR, LABEL_DIR)
