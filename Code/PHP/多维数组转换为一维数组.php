<?php

// 将多维数组转换为一维

function arr_foreach($arr) {
    static $data;
    if (!is_array ($arr)) {
        return $data;
    }
    foreach ($arr as $key => $val) {
        if (is_array($val)) {
            arr_foreach($val);
        } else {
            $data[] = $val;
        }
    }
    return $data;
}

?>