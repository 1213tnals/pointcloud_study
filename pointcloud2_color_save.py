import numpy as np
import trimesh

# 간격 설정
spacing = 2

# 포인트 클라우드 생성
x = np.arange(0, 100, spacing)
y = np.arange(0, 100, spacing)
z = np.arange(0, 100, spacing)

# 크기 설정
point_size = 0.1

# 컬러값 설정 (모든 점을 빨간색으로 설정)
color = np.array([1.0, 0.0, 0.0])

# 포인트 클라우드 생성
points = np.stack(np.meshgrid(x, y, z, indexing='ij'), axis=-1).reshape(-1, 3)
colors = np.tile(color, (len(points), 1))  # 모든 점에 동일한 색상 적용
point_cloud = trimesh.PointCloud(points, colors=colors, size=point_size)

# 시각화(씬)
scene = trimesh.Scene(point_cloud)      # 씬에다가 담음
scene.show()                            # 시각화 

# ply 파일로 저장
ply_file_path = "point_cloud.ply"
point_cloud.export(ply_file_path)
