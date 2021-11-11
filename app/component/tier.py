from typing import Final

UNKNOWN: Final = 0
BRONZE: Final = 1
SILVER: Final = 2
GOLD: Final = 3
PLATINUM: Final = 4
DIAMOND: Final = 5
RUBY: Final = 6
MASTER: Final = 7

__tier_badge_color: Final = {
    UNKNOWN: "#555",
    BRONZE: "#7A3C00",
    SILVER: "#8CB6FF",
    GOLD: "#FFD800",
    PLATINUM: "#2CFFE3",
    DIAMOND: "#00B4FC",
    RUBY: "#FF0062",
    MASTER: "#EE99FF",
}

__tier_text: Final = {
    0: "Unknown",
    1: "Bronze V",
    2: "Bronze IV",
    3: "Bronze III",
    4: "Bronze II",
    5: "Bronze I",
    6: "Silver V",
    7: "Silver IV",
    8: "Silver III",
    9: "Silver II",
    10: "Silver I",
    11: "Gold V",
    12: "Gold IV",
    13: "Gold III",
    14: "Gold II",
    15: "Gold I",
    16: "Platinum V",
    17: "Platinum IV",
    18: "Platinum III",
    19: "Platinum II",
    20: "Platinum I",
    21: "Diamond V",
    22: "Diamond IV",
    23: "Diamond III",
    24: "Diamond II",
    25: "Diamond I",
    26: "Ruby V",
    27: "Ruby IV",
    28: "Ruby III",
    29: "Ruby II",
    30: "Ruby I",
    31: "Master",
}

__tier_icon: Final = {
    0: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#2d2d2d;}.cls-2{fill:#fff;}</style></defs><title>0</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M291.8,133.59a68.54,68.54,0,0,1-2.89,20.88A62.48,62.48,0,0,1,280.75,171a81.44,81.44,0,0,1-12.67,14.22q-7.43,6.67-16.84,13.86c-3.86,3.12-7.07,5.89-9.6,8.28a33.26,33.26,0,0,0-6,7.38,27.63,27.63,0,0,0-3.07,7.92,46.64,46.64,0,0,0-.91,9.9V242H175.52V228.27a70.93,70.93,0,0,1,1.8-16.74,49.92,49.92,0,0,1,5.4-13.5,72.82,72.82,0,0,1,8.82-11.88A135.7,135.7,0,0,1,204,174.27l11.88-11.16a70.45,70.45,0,0,0,10.44-11.34,23.5,23.5,0,0,0,4.32-14.22q0-11.51-7-18.36t-19.26-6.84q-15.12,0-22.68,10.26a42.26,42.26,0,0,0-8.28,23.22l-57.24-6.12q2.16-19.44,9.9-34.2A75.63,75.63,0,0,1,146,81a85.14,85.14,0,0,1,27.74-14.58,109.22,109.22,0,0,1,32.84-4.86,121.18,121.18,0,0,1,31.6,4.14,80.58,80.58,0,0,1,27.26,13,65.91,65.91,0,0,1,19.14,22.5Q291.79,114.89,291.8,133.59ZM238.88,292.71A32.71,32.71,0,0,1,228.8,317q-10.08,9.9-24.84,9.9a36,36,0,0,1-13.5-2.52,34,34,0,0,1-11.16-7.2,36.11,36.11,0,0,1-7.74-10.8,30.82,30.82,0,0,1-2.88-13.32,33.09,33.09,0,0,1,2.7-13.14,33.48,33.48,0,0,1,7.56-11,36.48,36.48,0,0,1,11.34-7.38,35.21,35.21,0,0,1,13.68-2.7,33.91,33.91,0,0,1,13.5,2.7,39,39,0,0,1,11.16,7.2,31.55,31.55,0,0,1,7.56,10.8A33.09,33.09,0,0,1,238.88,292.71Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    1: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ad5600;}.cls-2{fill:#fff;}</style></defs><title>1</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M293.24,239.07q0,23.42-8.28,40.5a80.79,80.79,0,0,1-22.14,28.26,95.4,95.4,0,0,1-31.5,16.74,122,122,0,0,1-69.3,1.08,105,105,0,0,1-28.44-12.78,86.12,86.12,0,0,1-22-20.34,81.21,81.21,0,0,1-13.5-27.18l55.08-16.92a42.82,42.82,0,0,0,14.94,22q11,8.64,26.1,8.64a40.76,40.76,0,0,0,26.82-9.36Q232.4,260.33,232.4,242q0-11.14-4.68-18.72a36.31,36.31,0,0,0-12.06-12.06,50.2,50.2,0,0,0-16.74-6.3,98.92,98.92,0,0,0-18.72-1.8,183.54,183.54,0,0,0-31.14,3.06,181.34,181.34,0,0,0-31.14,8.1L124,68.43H280.28v51.84H177.68l-2.16,40.32a78.33,78.33,0,0,1,12.78-2q7-.54,12.78-.54a125.49,125.49,0,0,1,36,5,82.55,82.55,0,0,1,29.34,15.3A73.33,73.33,0,0,1,286,203.79Q293.24,218.91,293.24,239.07Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    2: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ad5600;}.cls-2{fill:#fff;}</style></defs><title>2</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M269.12,273.63v49.68H212.6V273.63H92.72V222.87L196.4,68.43h72.36V224.67H304v49ZM213,130.35h-1.08L151.4,224.67H213Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    3: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ad5600;}.cls-2{fill:#fff;}</style></defs><title>3</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M293.6,249.27q0,20.85-8.46,36.13A76,76,0,0,1,263,310.56a97.64,97.64,0,0,1-30.78,14.74,126.85,126.85,0,0,1-34.74,4.85,142.73,142.73,0,0,1-33.66-4,106.16,106.16,0,0,1-29.88-12.06,86.49,86.49,0,0,1-23.58-20.88q-10.08-12.76-15.12-30.78l56.16-14.76q3.6,12.61,14.76,22.14t28.44,9.54a49.79,49.79,0,0,0,13.14-1.8A35.92,35.92,0,0,0,219.62,272a30.07,30.07,0,0,0,8.64-9.9q3.42-6.11,3.42-15.12,0-9.72-4.5-16.2a31.87,31.87,0,0,0-11.88-10.26,58.34,58.34,0,0,0-16.74-5.4,109.58,109.58,0,0,0-18.72-1.62h-16.2V169.59h17.64a105.32,105.32,0,0,0,16.56-1.26,44.11,44.11,0,0,0,14.22-4.71,27.61,27.61,0,0,0,10.08-9.24q3.78-5.79,3.78-15.21,0-13.77-9.72-21a36.36,36.36,0,0,0-22.32-7.25,34.62,34.62,0,0,0-22.5,7.74A35.77,35.77,0,0,0,159,139.35l-56.16-13a83.31,83.31,0,0,1,14-28.26A86.36,86.36,0,0,1,139,78a102.2,102.2,0,0,1,27.9-12.24,117.12,117.12,0,0,1,31-4.14,126,126,0,0,1,32.94,4.33A88.14,88.14,0,0,1,259.4,79.26a70.38,70.38,0,0,1,20.34,22.53q7.74,13.53,7.74,31.91,0,21.28-12.06,35.88a58.73,58.73,0,0,1-30.78,19.64v1.08a65.79,65.79,0,0,1,19.8,8.09,63.92,63.92,0,0,1,15.48,13.31A59.22,59.22,0,0,1,290,229,57,57,0,0,1,293.6,249.27Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    4: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ad5600;}.cls-2{fill:#fff;}</style></defs><title>4</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M108.2,323.31V273l99.36-89.85a93.82,93.82,0,0,0,15.12-18.33A38.88,38.88,0,0,0,228.44,144q0-13.65-8.64-22.1t-23-8.45q-15.12,0-24.66,10.62T160.76,152l-58-7.92a91,91,0,0,1,10.62-34.62,90,90,0,0,1,21.42-25.89,92.61,92.61,0,0,1,29.7-16.31A110.86,110.86,0,0,1,200,61.59a125.53,125.53,0,0,1,34.2,4.68,89.24,89.24,0,0,1,29.52,14.4,71.88,71.88,0,0,1,20.7,24.48q7.74,14.77,7.74,34.56a78.88,78.88,0,0,1-3.6,24.66,81.62,81.62,0,0,1-9.9,20.34,116.69,116.69,0,0,1-14.4,17.46q-8.1,8.1-16.74,16l-59,52.56h104v52.56Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    5: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ad5600;}.cls-2{fill:#fff;}</style></defs><title>5</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M185.6,323.31V136.11l-47.52,36.72L106.76,130l83.85-61.56h55.11V323.31Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    6: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#435f7a;}.cls-2{fill:#fff;}</style></defs><title>6</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M293.24,239.07q0,23.42-8.28,40.5a80.79,80.79,0,0,1-22.14,28.26,95.4,95.4,0,0,1-31.5,16.74,122,122,0,0,1-69.3,1.08,105,105,0,0,1-28.44-12.78,86.12,86.12,0,0,1-22-20.34,81.21,81.21,0,0,1-13.5-27.18l55.08-16.92a42.82,42.82,0,0,0,14.94,22q11,8.64,26.1,8.64a40.76,40.76,0,0,0,26.82-9.36Q232.4,260.33,232.4,242q0-11.14-4.68-18.72a36.31,36.31,0,0,0-12.06-12.06,50.2,50.2,0,0,0-16.74-6.3,98.92,98.92,0,0,0-18.72-1.8,183.54,183.54,0,0,0-31.14,3.06,181.34,181.34,0,0,0-31.14,8.1L124,68.43H280.28v51.84H177.68l-2.16,40.32a78.33,78.33,0,0,1,12.78-2q7-.54,12.78-.54a125.49,125.49,0,0,1,36,5,82.55,82.55,0,0,1,29.34,15.3A73.33,73.33,0,0,1,286,203.79Q293.24,218.91,293.24,239.07Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    7: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#435f7a;}.cls-2{fill:#fff;}</style></defs><title>7</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M269.12,273.63v49.68H212.6V273.63H92.72V222.87L196.4,68.43h72.36V224.67H304v49ZM213,130.35h-1.08L151.4,224.67H213Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    8: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#435f7a;}.cls-2{fill:#fff;}</style></defs><title>8</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M293.6,249.27q0,20.85-8.46,36.13A76,76,0,0,1,263,310.56a97.64,97.64,0,0,1-30.78,14.74,126.85,126.85,0,0,1-34.74,4.85,142.73,142.73,0,0,1-33.66-4,106.16,106.16,0,0,1-29.88-12.06,86.49,86.49,0,0,1-23.58-20.88q-10.08-12.76-15.12-30.78l56.16-14.76q3.6,12.61,14.76,22.14t28.44,9.54a49.79,49.79,0,0,0,13.14-1.8A35.92,35.92,0,0,0,219.62,272a30.07,30.07,0,0,0,8.64-9.9q3.42-6.11,3.42-15.12,0-9.72-4.5-16.2a31.87,31.87,0,0,0-11.88-10.26,58.34,58.34,0,0,0-16.74-5.4,109.58,109.58,0,0,0-18.72-1.62h-16.2V169.59h17.64a105.32,105.32,0,0,0,16.56-1.26,44.11,44.11,0,0,0,14.22-4.71,27.61,27.61,0,0,0,10.08-9.24q3.78-5.79,3.78-15.21,0-13.77-9.72-21a36.36,36.36,0,0,0-22.32-7.25,34.62,34.62,0,0,0-22.5,7.74A35.77,35.77,0,0,0,159,139.35l-56.16-13a83.31,83.31,0,0,1,14-28.26A86.36,86.36,0,0,1,139,78a102.2,102.2,0,0,1,27.9-12.24,117.12,117.12,0,0,1,31-4.14,126,126,0,0,1,32.94,4.33A88.14,88.14,0,0,1,259.4,79.26a70.38,70.38,0,0,1,20.34,22.53q7.74,13.53,7.74,31.91,0,21.28-12.06,35.88a58.73,58.73,0,0,1-30.78,19.64v1.08a65.79,65.79,0,0,1,19.8,8.09,63.92,63.92,0,0,1,15.48,13.31A59.22,59.22,0,0,1,290,229,57,57,0,0,1,293.6,249.27Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    9: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#435f7a;}.cls-2{fill:#fff;}</style></defs><title>9</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M108.2,323.31V273l99.36-89.85a93.82,93.82,0,0,0,15.12-18.33A38.88,38.88,0,0,0,228.44,144q0-13.65-8.64-22.1t-23-8.45q-15.12,0-24.66,10.62T160.76,152l-58-7.92a91,91,0,0,1,10.62-34.62,90,90,0,0,1,21.42-25.89,92.61,92.61,0,0,1,29.7-16.31A110.86,110.86,0,0,1,200,61.59a125.53,125.53,0,0,1,34.2,4.68,89.24,89.24,0,0,1,29.52,14.4,71.88,71.88,0,0,1,20.7,24.48q7.74,14.77,7.74,34.56a78.88,78.88,0,0,1-3.6,24.66,81.62,81.62,0,0,1-9.9,20.34,116.69,116.69,0,0,1-14.4,17.46q-8.1,8.1-16.74,16l-59,52.56h104v52.56Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    10: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#435f7a;}.cls-2{fill:#fff;}</style></defs><title>10</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M185.6,323.31V136.11l-47.52,36.72L106.76,130l83.85-61.56h55.11V323.31Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    11: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ec9a00;}.cls-2{fill:#fff;}</style></defs><title>11</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M293.24,239.07q0,23.42-8.28,40.5a80.79,80.79,0,0,1-22.14,28.26,95.4,95.4,0,0,1-31.5,16.74,122,122,0,0,1-69.3,1.08,105,105,0,0,1-28.44-12.78,86.12,86.12,0,0,1-22-20.34,81.21,81.21,0,0,1-13.5-27.18l55.08-16.92a42.82,42.82,0,0,0,14.94,22q11,8.64,26.1,8.64a40.76,40.76,0,0,0,26.82-9.36Q232.4,260.33,232.4,242q0-11.14-4.68-18.72a36.31,36.31,0,0,0-12.06-12.06,50.2,50.2,0,0,0-16.74-6.3,98.92,98.92,0,0,0-18.72-1.8,183.54,183.54,0,0,0-31.14,3.06,181.34,181.34,0,0,0-31.14,8.1L124,68.43H280.28v51.84H177.68l-2.16,40.32a78.33,78.33,0,0,1,12.78-2q7-.54,12.78-.54a125.49,125.49,0,0,1,36,5,82.55,82.55,0,0,1,29.34,15.3A73.33,73.33,0,0,1,286,203.79Q293.24,218.91,293.24,239.07Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    12: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ec9a00;}.cls-2{fill:#fff;}</style></defs><title>12</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M269.12,273.63v49.68H212.6V273.63H92.72V222.87L196.4,68.43h72.36V224.67H304v49ZM213,130.35h-1.08L151.4,224.67H213Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    13: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ec9a00;}.cls-2{fill:#fff;}</style></defs><title>13</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M293.6,249.27q0,20.85-8.46,36.13A76,76,0,0,1,263,310.56a97.64,97.64,0,0,1-30.78,14.74,126.85,126.85,0,0,1-34.74,4.85,142.73,142.73,0,0,1-33.66-4,106.16,106.16,0,0,1-29.88-12.06,86.49,86.49,0,0,1-23.58-20.88q-10.08-12.76-15.12-30.78l56.16-14.76q3.6,12.61,14.76,22.14t28.44,9.54a49.79,49.79,0,0,0,13.14-1.8A35.92,35.92,0,0,0,219.62,272a30.07,30.07,0,0,0,8.64-9.9q3.42-6.11,3.42-15.12,0-9.72-4.5-16.2a31.87,31.87,0,0,0-11.88-10.26,58.34,58.34,0,0,0-16.74-5.4,109.58,109.58,0,0,0-18.72-1.62h-16.2V169.59h17.64a105.32,105.32,0,0,0,16.56-1.26,44.11,44.11,0,0,0,14.22-4.71,27.61,27.61,0,0,0,10.08-9.24q3.78-5.79,3.78-15.21,0-13.77-9.72-21a36.36,36.36,0,0,0-22.32-7.25,34.62,34.62,0,0,0-22.5,7.74A35.77,35.77,0,0,0,159,139.35l-56.16-13a83.31,83.31,0,0,1,14-28.26A86.36,86.36,0,0,1,139,78a102.2,102.2,0,0,1,27.9-12.24,117.12,117.12,0,0,1,31-4.14,126,126,0,0,1,32.94,4.33A88.14,88.14,0,0,1,259.4,79.26a70.38,70.38,0,0,1,20.34,22.53q7.74,13.53,7.74,31.91,0,21.28-12.06,35.88a58.73,58.73,0,0,1-30.78,19.64v1.08a65.79,65.79,0,0,1,19.8,8.09,63.92,63.92,0,0,1,15.48,13.31A59.22,59.22,0,0,1,290,229,57,57,0,0,1,293.6,249.27Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    14: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ec9a00;}.cls-2{fill:#fff;}</style></defs><title>14</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M108.2,323.31V273l99.36-89.85a93.82,93.82,0,0,0,15.12-18.33A38.88,38.88,0,0,0,228.44,144q0-13.65-8.64-22.1t-23-8.45q-15.12,0-24.66,10.62T160.76,152l-58-7.92a91,91,0,0,1,10.62-34.62,90,90,0,0,1,21.42-25.89,92.61,92.61,0,0,1,29.7-16.31A110.86,110.86,0,0,1,200,61.59a125.53,125.53,0,0,1,34.2,4.68,89.24,89.24,0,0,1,29.52,14.4,71.88,71.88,0,0,1,20.7,24.48q7.74,14.77,7.74,34.56a78.88,78.88,0,0,1-3.6,24.66,81.62,81.62,0,0,1-9.9,20.34,116.69,116.69,0,0,1-14.4,17.46q-8.1,8.1-16.74,16l-59,52.56h104v52.56Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    15: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ec9a00;}.cls-2{fill:#fff;}</style></defs><title>15</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M185.6,323.31V136.11l-47.52,36.72L106.76,130l83.85-61.56h55.11V323.31Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    16: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#27e2a4;}.cls-2{fill:#fff;}</style></defs><title>16</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/><path class=\"cls-2\" d=\"M293.24,239.07q0,23.42-8.28,40.5a80.79,80.79,0,0,1-22.14,28.26,95.4,95.4,0,0,1-31.5,16.74,122,122,0,0,1-69.3,1.08,105,105,0,0,1-28.44-12.78,86.12,86.12,0,0,1-22-20.34,81.21,81.21,0,0,1-13.5-27.18l55.08-16.92a42.82,42.82,0,0,0,14.94,22q11,8.64,26.1,8.64a40.76,40.76,0,0,0,26.82-9.36Q232.4,260.33,232.4,242q0-11.14-4.68-18.72a36.31,36.31,0,0,0-12.06-12.06,50.2,50.2,0,0,0-16.74-6.3,98.92,98.92,0,0,0-18.72-1.8,183.54,183.54,0,0,0-31.14,3.06,181.34,181.34,0,0,0-31.14,8.1L124,68.43H280.28v51.84H177.68l-2.16,40.32a78.33,78.33,0,0,1,12.78-2q7-.54,12.78-.54a125.49,125.49,0,0,1,36,5,82.55,82.55,0,0,1,29.34,15.3A73.33,73.33,0,0,1,286,203.79Q293.24,218.91,293.24,239.07Z\" transform=\"translate(0)\"/></svg>",
    17: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#27e2a4;}.cls-2{fill:#fff;}</style></defs><title>17</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/><path class=\"cls-2\" d=\"M269.12,273.63v49.68H212.6V273.63H92.72V222.87L196.4,68.43h72.36V224.67H304v49ZM213,130.35h-1.08L151.4,224.67H213Z\" transform=\"translate(0)\"/></svg>",
    18: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#27e2a4;}.cls-2{fill:#fff;}</style></defs><title>18</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/><path class=\"cls-2\" d=\"M293.6,249.27q0,20.85-8.46,36.13A76,76,0,0,1,263,310.56a97.64,97.64,0,0,1-30.78,14.74,126.85,126.85,0,0,1-34.74,4.85,142.73,142.73,0,0,1-33.66-4,106.16,106.16,0,0,1-29.88-12.06,86.49,86.49,0,0,1-23.58-20.88q-10.08-12.76-15.12-30.78l56.16-14.76q3.6,12.61,14.76,22.14t28.44,9.54a49.79,49.79,0,0,0,13.14-1.8A35.92,35.92,0,0,0,219.62,272a30.07,30.07,0,0,0,8.64-9.9q3.42-6.11,3.42-15.12,0-9.72-4.5-16.2a31.87,31.87,0,0,0-11.88-10.26,58.34,58.34,0,0,0-16.74-5.4,109.58,109.58,0,0,0-18.72-1.62h-16.2V169.59h17.64a105.32,105.32,0,0,0,16.56-1.26,44.11,44.11,0,0,0,14.22-4.71,27.61,27.61,0,0,0,10.08-9.24q3.78-5.79,3.78-15.21,0-13.77-9.72-21a36.36,36.36,0,0,0-22.32-7.25,34.62,34.62,0,0,0-22.5,7.74A35.77,35.77,0,0,0,159,139.35l-56.16-13a83.31,83.31,0,0,1,14-28.26A86.36,86.36,0,0,1,139,78a102.2,102.2,0,0,1,27.9-12.24,117.12,117.12,0,0,1,31-4.14,126,126,0,0,1,32.94,4.33A88.14,88.14,0,0,1,259.4,79.26a70.38,70.38,0,0,1,20.34,22.53q7.74,13.53,7.74,31.91,0,21.28-12.06,35.88a58.73,58.73,0,0,1-30.78,19.64v1.08a65.79,65.79,0,0,1,19.8,8.09,63.92,63.92,0,0,1,15.48,13.31A59.22,59.22,0,0,1,290,229,57,57,0,0,1,293.6,249.27Z\" transform=\"translate(0)\"/></svg>",
    19: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#27e2a4;}.cls-2{fill:#fff;}</style></defs><title>19</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/><path class=\"cls-2\" d=\"M108.2,323.31V273l99.36-89.85a93.82,93.82,0,0,0,15.12-18.33A38.88,38.88,0,0,0,228.44,144q0-13.65-8.64-22.1t-23-8.45q-15.12,0-24.66,10.62T160.76,152l-58-7.92a91,91,0,0,1,10.62-34.62,90,90,0,0,1,21.42-25.89,92.61,92.61,0,0,1,29.7-16.31A110.86,110.86,0,0,1,200,61.59a125.53,125.53,0,0,1,34.2,4.68,89.24,89.24,0,0,1,29.52,14.4,71.88,71.88,0,0,1,20.7,24.48q7.74,14.77,7.74,34.56a78.88,78.88,0,0,1-3.6,24.66,81.62,81.62,0,0,1-9.9,20.34,116.69,116.69,0,0,1-14.4,17.46q-8.1,8.1-16.74,16l-59,52.56h104v52.56Z\" transform=\"translate(0)\"/></svg>",
    20: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#27e2a4;}.cls-2{fill:#fff;}</style></defs><title>20</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/><path class=\"cls-2\" d=\"M185.6,323.31V136.11l-47.52,36.72L106.76,130l83.85-61.56h55.11V323.31Z\" transform=\"translate(0)\"/></svg>",
    21: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#00b4fc;}.cls-2{fill:#fff;}</style></defs><title>21</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M293.24,239.07q0,23.42-8.28,40.5a80.79,80.79,0,0,1-22.14,28.26,95.4,95.4,0,0,1-31.5,16.74,122,122,0,0,1-69.3,1.08,105,105,0,0,1-28.44-12.78,86.12,86.12,0,0,1-22-20.34,81.21,81.21,0,0,1-13.5-27.18l55.08-16.92a42.82,42.82,0,0,0,14.94,22q11,8.64,26.1,8.64a40.76,40.76,0,0,0,26.82-9.36Q232.4,260.33,232.4,242q0-11.14-4.68-18.72a36.31,36.31,0,0,0-12.06-12.06,50.2,50.2,0,0,0-16.74-6.3,98.92,98.92,0,0,0-18.72-1.8,183.54,183.54,0,0,0-31.14,3.06,181.34,181.34,0,0,0-31.14,8.1L124,68.43H280.28v51.84H177.68l-2.16,40.32a78.33,78.33,0,0,1,12.78-2q7-.54,12.78-.54a125.49,125.49,0,0,1,36,5,82.55,82.55,0,0,1,29.34,15.3A73.33,73.33,0,0,1,286,203.79Q293.24,218.91,293.24,239.07Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    22: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#00b4fc;}.cls-2{fill:#fff;}</style></defs><title>22</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M269.12,273.63v49.68H212.6V273.63H92.72V222.87L196.4,68.43h72.36V224.67H304v49ZM213,130.35h-1.08L151.4,224.67H213Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    23: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#00b4fc;}.cls-2{fill:#fff;}</style></defs><title>23</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M293.6,249.27q0,20.85-8.46,36.13A76,76,0,0,1,263,310.56a97.64,97.64,0,0,1-30.78,14.74,126.85,126.85,0,0,1-34.74,4.85,142.73,142.73,0,0,1-33.66-4,106.16,106.16,0,0,1-29.88-12.06,86.49,86.49,0,0,1-23.58-20.88q-10.08-12.76-15.12-30.78l56.16-14.76q3.6,12.61,14.76,22.14t28.44,9.54a49.79,49.79,0,0,0,13.14-1.8A35.92,35.92,0,0,0,219.62,272a30.07,30.07,0,0,0,8.64-9.9q3.42-6.11,3.42-15.12,0-9.72-4.5-16.2a31.87,31.87,0,0,0-11.88-10.26,58.34,58.34,0,0,0-16.74-5.4,109.58,109.58,0,0,0-18.72-1.62h-16.2V169.59h17.64a105.32,105.32,0,0,0,16.56-1.26,44.11,44.11,0,0,0,14.22-4.71,27.61,27.61,0,0,0,10.08-9.24q3.78-5.79,3.78-15.21,0-13.77-9.72-21a36.36,36.36,0,0,0-22.32-7.25,34.62,34.62,0,0,0-22.5,7.74A35.77,35.77,0,0,0,159,139.35l-56.16-13a83.31,83.31,0,0,1,14-28.26A86.36,86.36,0,0,1,139,78a102.2,102.2,0,0,1,27.9-12.24,117.12,117.12,0,0,1,31-4.14,126,126,0,0,1,32.94,4.33A88.14,88.14,0,0,1,259.4,79.26a70.38,70.38,0,0,1,20.34,22.53q7.74,13.53,7.74,31.91,0,21.28-12.06,35.88a58.73,58.73,0,0,1-30.78,19.64v1.08a65.79,65.79,0,0,1,19.8,8.09,63.92,63.92,0,0,1,15.48,13.31A59.22,59.22,0,0,1,290,229,57,57,0,0,1,293.6,249.27Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    24: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#00b4fc;}.cls-2{fill:#fff;}</style></defs><title>24</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M108.2,323.31V273l99.36-89.85a93.82,93.82,0,0,0,15.12-18.33A38.88,38.88,0,0,0,228.44,144q0-13.65-8.64-22.1t-23-8.45q-15.12,0-24.66,10.62T160.76,152l-58-7.92a91,91,0,0,1,10.62-34.62,90,90,0,0,1,21.42-25.89,92.61,92.61,0,0,1,29.7-16.31A110.86,110.86,0,0,1,200,61.59a125.53,125.53,0,0,1,34.2,4.68,89.24,89.24,0,0,1,29.52,14.4,71.88,71.88,0,0,1,20.7,24.48q7.74,14.77,7.74,34.56a78.88,78.88,0,0,1-3.6,24.66,81.62,81.62,0,0,1-9.9,20.34,116.69,116.69,0,0,1-14.4,17.46q-8.1,8.1-16.74,16l-59,52.56h104v52.56Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    25: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#00b4fc;}.cls-2{fill:#fff;}</style></defs><title>25</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M185.6,323.31V136.11l-47.52,36.72L106.76,130l83.85-61.56h55.11V323.31Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    26: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ff0062;}.cls-2{fill:#fff;}</style></defs><title>26</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M293.24,239.07q0,23.42-8.28,40.5a80.79,80.79,0,0,1-22.14,28.26,95.4,95.4,0,0,1-31.5,16.74,122,122,0,0,1-69.3,1.08,105,105,0,0,1-28.44-12.78,86.12,86.12,0,0,1-22-20.34,81.21,81.21,0,0,1-13.5-27.18l55.08-16.92a42.82,42.82,0,0,0,14.94,22q11,8.64,26.1,8.64a40.76,40.76,0,0,0,26.82-9.36Q232.4,260.33,232.4,242q0-11.14-4.68-18.72a36.31,36.31,0,0,0-12.06-12.06,50.2,50.2,0,0,0-16.74-6.3,98.92,98.92,0,0,0-18.72-1.8,183.54,183.54,0,0,0-31.14,3.06,181.34,181.34,0,0,0-31.14,8.1L124,68.43H280.28v51.84H177.68l-2.16,40.32a78.33,78.33,0,0,1,12.78-2q7-.54,12.78-.54a125.49,125.49,0,0,1,36,5,82.55,82.55,0,0,1,29.34,15.3A73.33,73.33,0,0,1,286,203.79Q293.24,218.91,293.24,239.07Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    27: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ff0062;}.cls-2{fill:#fff;}</style></defs><title>27</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M269.12,273.63v49.68H212.6V273.63H92.72V222.87L196.4,68.43h72.36V224.67H304v49ZM213,130.35h-1.08L151.4,224.67H213Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    28: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ff0062;}.cls-2{fill:#fff;}</style></defs><title>28</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M293.6,249.27q0,20.85-8.46,36.13A76,76,0,0,1,263,310.56a97.64,97.64,0,0,1-30.78,14.74,126.85,126.85,0,0,1-34.74,4.85,142.73,142.73,0,0,1-33.66-4,106.16,106.16,0,0,1-29.88-12.06,86.49,86.49,0,0,1-23.58-20.88q-10.08-12.76-15.12-30.78l56.16-14.76q3.6,12.61,14.76,22.14t28.44,9.54a49.79,49.79,0,0,0,13.14-1.8A35.92,35.92,0,0,0,219.62,272a30.07,30.07,0,0,0,8.64-9.9q3.42-6.11,3.42-15.12,0-9.72-4.5-16.2a31.87,31.87,0,0,0-11.88-10.26,58.34,58.34,0,0,0-16.74-5.4,109.58,109.58,0,0,0-18.72-1.62h-16.2V169.59h17.64a105.32,105.32,0,0,0,16.56-1.26,44.11,44.11,0,0,0,14.22-4.71,27.61,27.61,0,0,0,10.08-9.24q3.78-5.79,3.78-15.21,0-13.77-9.72-21a36.36,36.36,0,0,0-22.32-7.25,34.62,34.62,0,0,0-22.5,7.74A35.77,35.77,0,0,0,159,139.35l-56.16-13a83.31,83.31,0,0,1,14-28.26A86.36,86.36,0,0,1,139,78a102.2,102.2,0,0,1,27.9-12.24,117.12,117.12,0,0,1,31-4.14,126,126,0,0,1,32.94,4.33A88.14,88.14,0,0,1,259.4,79.26a70.38,70.38,0,0,1,20.34,22.53q7.74,13.53,7.74,31.91,0,21.28-12.06,35.88a58.73,58.73,0,0,1-30.78,19.64v1.08a65.79,65.79,0,0,1,19.8,8.09,63.92,63.92,0,0,1,15.48,13.31A59.22,59.22,0,0,1,290,229,57,57,0,0,1,293.6,249.27Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    29: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ff0062;}.cls-2{fill:#fff;}</style></defs><title>29</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M108.2,323.31V273l99.36-89.85a93.82,93.82,0,0,0,15.12-18.33A38.88,38.88,0,0,0,228.44,144q0-13.65-8.64-22.1t-23-8.45q-15.12,0-24.66,10.62T160.76,152l-58-7.92a91,91,0,0,1,10.62-34.62,90,90,0,0,1,21.42-25.89,92.61,92.61,0,0,1,29.7-16.31A110.86,110.86,0,0,1,200,61.59a125.53,125.53,0,0,1,34.2,4.68,89.24,89.24,0,0,1,29.52,14.4,71.88,71.88,0,0,1,20.7,24.48q7.74,14.77,7.74,34.56a78.88,78.88,0,0,1-3.6,24.66,81.62,81.62,0,0,1-9.9,20.34,116.69,116.69,0,0,1-14.4,17.46q-8.1,8.1-16.74,16l-59,52.56h104v52.56Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    30: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><defs><style>.cls-1{fill:#ff0062;}.cls-2{fill:#fff;}</style></defs><title>30</title><polygon class=\"cls-1\" points=\"0 0 0 419.74 199.77 512 400 419.74 400 0 0 0\"/><path class=\"cls-2\" d=\"M185.6,323.31V136.11l-47.52,36.72L106.76,130l83.85-61.56h55.11V323.31Z\" transform=\"translate(0)\"/><polygon class=\"cls-2\" points=\"0 339.02 0 378.94 199.77 471.2 400 378.94 400 339.02 199.77 431.28 0 339.02\"/></svg>",
    31: "<svg id=\"레이어_1\" data-name=\"레이어 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 512\"><style type=\"text/css\">.st0{fill:url(#SVGID_1_)}.st1{fill:#FFFFFF}</style><linearGradient id=\"SVGID_1_\" gradientUnits=\"userSpaceOnUse\" x1=\"200\" y1=\"512\" x2=\"200\" y2=\"4.325293e-06\"><stop offset=\"0\" style=\"stop-color:#FF7CA8\"></stop><stop offset=\"0.5\" style=\"stop-color:#B491FF\"></stop><stop offset=\"1\" style=\"stop-color:#7CF9FF\"></stop></linearGradient><polygon class=\"st0\" points=\"0,0 0,419.7 199.8,512 400,419.7 400,0\"></polygon><g><path class=\"st1\" d=\"M72,83.7h75.5l52.2,147.8h0.6l52.5-147.8H328v226.6h-49.9V136.5h-0.6l-59.5,173.8h-38.1l-57.3-173.8h-0.6 v173.8H72V83.7z\"></path></g><polygon class=\"st1\" points=\"0,339 0,378.9 199.8,471.2 400,378.9 400,339 199.8,431.3\"></polygon></svg>",
}


def get_tier_text(level: int) -> str:
    if level in __tier_text:
        return __tier_text[level]
    else:
        return __tier_text[0]


def get_tier_icon(level: int) -> str:
    if level in __tier_icon:
        return __tier_icon[level]
    else:
        return __tier_icon[0]


def __get_tier_section(level: int) -> int:
    if level <= 0:
        return UNKNOWN
    elif level <= 5:
        return BRONZE
    elif level <= 10:
        return SILVER
    elif level <= 15:
        return GOLD
    elif level <= 20:
        return PLATINUM
    elif level <= 25:
        return DIAMOND
    elif level <= 30:
        return RUBY
    elif level <= 31:
        return MASTER
    else:
        return UNKNOWN


def get_tier_hex_color(level: int) -> str:
    section = __get_tier_section(level)
    return __tier_badge_color[section]