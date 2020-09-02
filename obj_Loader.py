# objファイルから頂点情報を抽出するプログラム

import json

def main():
    vertex_indices = []
    tex_coord = []
    normals = []
    faces = []

    # 入力ファイル指定
    print("Input file name -> ", end="")
    in_file = input()
    #in_file = 'sample/sample.obj'  # Debug
    f = open(in_file, "r")

    # 頂点情報を抽出
    lines = f.read().split()
    temp = []
    for i, item in enumerate(lines):
        if item == 'v':
            vertex_indices.append([float(lines[i+1]), float(lines[i+2]), float(lines[i+3])])
        elif item == 'vt':
            tex_coord.append([float(lines[i+1]), float(lines[i+2])])
        elif item == 'vn':
            normals.append([float(lines[i+1]), float(lines[i+2]), float(lines[i+3])])
        elif item == 'f':
            faces.append([int(lines[i+1].split('/')[0]), int(lines[i+1].split('/')[1]),
                         int(lines[i+1].split('/')[2])])
            faces.append([int(lines[i+2].split('/')[0]), int(lines[i+2].split('/')[1]),
                         int(lines[i+2].split('/')[2])])
            faces.append([int(lines[i+3].split('/')[0]), int(lines[i+3].split('/')[1]),
                         int(lines[i+3].split('/')[2])])
            faces.append([int(lines[i+4].split('/')[0]), int(lines[i+4].split('/')[1]),
                         int(lines[i+4].split('/')[2])])

    # json用データを整形
    json_data = { "verts" : vertex_indices,
                  "tex_coord" : tex_coord,
                  "normals" : normals,
                  "faces" : faces }

    # jsonファイルを指定先に出力
    print("Output file name -> ", end="")
    out_name = input()
    #out_name = 'sample/sample.json'  # Debug
    fp = open(out_name, "w")
    json_data = json.dump(json_data, fp, indent=4)

    fp.close()
    f.close()


if __name__ == '__main__':
    main()
