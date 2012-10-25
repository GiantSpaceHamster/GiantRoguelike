from core import *
from utils import *

# 아래와 같은 맵을 만든다.
#[][][][][][]
#[]        []
#[]        []
#[]        []
#[][][][][][]
#
# 1. 맵 구조 생성은 1층 부분에서 이루어 진다.
# 2. 벽과 같은 구조는 1층을 참고하여 3층에 이루어진다.
# 3. 나머지 아이템들 역시 1층과 3층을 참고하여 각각 생성 된다.
# 4. 마지막으로 캐릭터들이 1층과 3층을 참고하여 3층에 배치가 된다.
# 5. 이때, 각 오브젝트들은 자신의 위치를 안다.
player = PlayerCharacter()
player.SetPosition(2, 2)
player.SetProperty("ResourceID", "Image/BlockObject/PlayableCharacter/Character/warrior")

"""
fieldMap = [
        [
            [ Wall(), Wall(), Door(), Wall(), Wall() ],
            [ Wall(), Object(), Object(), Object(), Wall() ],
            [ Wall(), Object(), Object(), Object(), Wall() ],
            [ Wall(), Object(), Object(), Object(), Wall() ],
            [ Wall(), Wall(), Wall(), Wall(), Wall() ]
        ]
    ,
        [
            [ Object(), Object(), Object(), Object(), Object() ],
            [ Object(), Object(), Object(), Object(), Object() ],
            [ Object(), Object(), Object(), Object(), Object() ],
            [ Object(), Object(), Object(), Object(), Object() ],
            [ Object(), Object(), Object(), Object(), Object() ]
        ]
    ,
        [
            [ Board(), Board(), Board(), Board(), Board() ],
            [ Board(), Board(), Board(), Board(), Board() ],
            [ Board(), Board(), Board(), Board(), Board() ],
            [ Board(), Board(), Board(), Board(), Board() ],
            [ Board(), Board(), Board(), Board(), Board() ]
        ]
    ]
"""

row = 10
col = 10

fieldMap = [[], [], []]
GenerateMap(row, col, fieldMap)            

fieldMap[0][player.GetX()][player.GetY()] = player
fieldMap[0][4][4] = EnemyCharacter()
