from collections import Counter

def load_file_to_lookup(path):
    file = open('b_lovely_landscapes.txt', mode='r')
    lines = file.read().splitlines()
    file.close()
    imgs = []
    all_tags = []
    hv = []
    for line in lines[1:]:
        line = line.split(' ')
        # hv.append(line[0])
        if line[0] == 'H':
            imgs.append(line[2:])
            all_tags.extend(line[2:])

    unique_tags = set(all_tags)
    return imgs, {i: tag for i, tag in enumerate(unique_tags)}
    # for i, tag in enumerate(unique_tags):
    #     print(i, tag)
    #     lookup_tags[i] = tag
    # data = pd.read_csv(path)
    # nums = data.values
    # tags = []
    # for i in range(nums.shape[0]):
    #     row = nums[i]
    #     # for tag in range(row[-1])

    # for row in np.nditer(nums, flags=["refs_OK"], op_flags=["readwrite"]):
    #     print(row)

def get_tags_count(lookup, data):
    score = []
    rows = []
    for row in data:
        rows.extend(row)
    return Counter(rows)
    # arr = np.array(np.array(row) for row in data)
    # for value in lookup.values():
    #     unique, counts = np.unique(value, return_counts=True)
    #     print(unique[0], counts)
    # dict(zip(unique, counts))


def get_img_abs_score(data):
    total_scores = {}
    for i, img in enumerate(imgs_data):
        img_score = 0
        for tag in img:
            img_score += tags_count.get(tag) - 1
        total_scores[i] = img_score
    return total_scores


if __name__ == '__main__':
    # file_path = os.path.join(os.path.dirname(__file__), )
    # data = pd.read_csv('b_lovely_landscapes.txt')
    # data.head()
    paths = ['b_lovely_landscapes.txt', 'c_memorable_moments.txt', 'd_pet_pictures.txt', 'e_shiny_selfies.txt']
    imgs_data, lookup_tags = load_file_to_lookup(paths[0])
    tags_count = get_tags_count(lookup_tags, imgs_data)
    img_scores = get_img_abs_score(imgs_data)
    max_val = max(img_scores.values())
    seed = -1
    for img, score in img_scores.items():
        if score == max_val:
            seed = img
    # find the line tags for seed img
    seed_tags = imgs_data[seed]

    #  create hash table tag to images
    # tag_to_imgs = {}
    # for index, tag in lookup_tags.items():
    #     for i, row in enumerate(imgs_data):
    #         if tag in row:
    #             # tag_to_imgs[tag] = [i] if tag_to_imgs.keys().__contains__(tag) == False else tag_to_imgs[tag].append(i)
    slides = [seed]
    # Add slide with same tag
    for index, tag in lookup_tags.items():
        for i, row in enumerate(imgs_data):
            if tag in row:
                slides.append(i)
    print(slides)
    out_tokens = paths[0].split(sep='.')
    out_name = out_tokens[0] + '_out.' + out_tokens[1]
    file = open(out_name, 'w+')
    file.write(str(len(slides)) + '\n')
    for slide in slides:
        file.write(str(len(slides)) + '\n')

    # for tag in seed_tags:
    #     for img in imgs_data:
    #         if tag in img: