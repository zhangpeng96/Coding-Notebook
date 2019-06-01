# bilibili 直播 API

### 直播间信息

`https://api.live.bilibili.com/room/v1/Room/room_init?id=<ROOMID>`

方法：`GET`

```json
{
	"code": 0,
	"msg": "ok",
	"message": "ok",
	"data": {
		"room_id": 383045,
		"short_id": 0,
		"uid": 26849519,
		"need_p2p": 0,
		"is_hidden": false,
		"is_locked": false,
		"is_portrait": false,
		"live_status": 1,
		"hidden_till": 0,
		"lock_till": 0,
		"encrypted": false,
		"pwd_verified": false,
		"live_time": 1559392122,
		"room_shield": 1,
		"is_sp": 0,
		"special_type": 0
	}
}
```

信息不够全面，可以用Android的api：

`https://api.live.bilibili.com/AppRoom/index?platform=android&room_id=<ROOMID>`

方法：`GET`

```json
{
	"code": 0,
	"data": {
		"room_id": 383045,
		"title": "Team E 苏杉杉生日公演",
		"cover": "https://i0.hdslb.com/bfs/live/room_cover/639a24af93174e2d581dcb7def754636d77a95c7.jpg",
		"mid": 26849519,
		"uname": "BEJ48",
		"face": "https://i0.hdslb.com/bfs/face/a063d55bc3d0d5c9d3cf55d2b9217050c42ae6fd.jpg",
		"m_face": "https://i0.hdslb.com/bfs/face/a063d55bc3d0d5c9d3cf55d2b9217050c42ae6fd.jpg",
		"background_id": 1,
		"attention": 37140,
		"is_attention": 1,
		"online": 10954,
		"create": 1467705085,
		"create_at": "2016-07-05 15:51:25",
		"sch_id": 0,
		"status": "LIVE",
		"area": "御宅文化",
		"area_id": 2,
		"area_v2_id": 143,
		"area_v2_parent_id": 1,
		"area_v2_name": "才艺",
		"area_v2_parent_name": "娱乐",
		"schedule": {
			"cid": 10383045,
			"sch_id": 0,
			"title": "Team E 苏杉杉生日公演",
			"mid": 26849519,
			"manager": [],
			"start": 1467705085,
			"start_at": "2016-07-05 15:51:25",
			"aid": 0,
			"stream_id": 374104,
			"online": 10954,
			"status": "LIVE",
			"meta_id": 0,
			"pending_meta_id": 0
		},
		"meta": {
			"tag": [],
			"description": "<p> </p>\n<p>BEJ48作为SNH48的姐妹团，取名自“Beijing”的拼音缩写，充分吸<span style=\"line-height: 1.45em; background-color: initial;\">取集团四年来沉淀的运营模式，并进行本土化改造，以“梦想、汗</span><span style=\"line-height: 1.45em; background-color: initial;\">水、坚持”为核心理念，通过每周BEJ48星梦剧院的公演，培育兼具</span><span style=\"line-height: 1.45em; background-color: initial;\">音乐、舞蹈、表演等才艺的全方位偶像，全力打造一支充满正能量</span><span style=\"line-height: 1.45em; background-color: initial;\">与青春活力的全球华语区第一女子偶像团体，努力实现成为北京文</span><span style=\"line-height: 1.45em; background-color: initial;\">化新名片及国民偶像的梦想。</span></p>\n<p> </p>",
			"typeid": 1,
			"tag_ids": {
				"0": 24
			},
			"cover": "https://i0.hdslb.com/bfs/live/room_cover/639a24af93174e2d581dcb7def754636d77a95c7.jpg",
			"check_status": "VERIFY",
			"aid": 0
		},
		"cmt": "livecmt-2.bilibili.com",
		"cmt_port": 88,
		"cmt_port_goim": 2243,
		"recommend": [
			{
				"owner": {
					"face": "https://i2.hdslb.com/bfs/face/5e0ab59a4d1461ee9431ebfa9cd6ca81693c674d.jpg",
					"mid": 424162531,
					"name": "二宫泡泡"
				},
				"cover": {
					"src": "https://i0.hdslb.com/bfs/live/21388712.jpg?06012036"
				},
				"title": "养一只我吧，我很乖哒",
				"room_id": 21388712,
				"online": 9503
			},
			{
				"owner": {
					"face": "https://i2.hdslb.com/bfs/face/b5e223c5e21293f53ff5a2308968343304d4ea49.jpg",
					"mid": 429563743,
					"name": "司雯S"
				},
				"cover": {
					"src": "https://i0.hdslb.com/bfs/live/21400321.jpg?06012036"
				},
				"title": "三十六线渣渣主播开播了",
				"room_id": 21400321,
				"online": 7538
			}
		],
		"toplist": [],
		"isvip": 0,
		"opentime": 1198,
		"prepare": "主播正在梳妆打扮中...",
		"isadmin": 0,
		"hot_word": [
			{
				"id": 50,
				"words": "队友呢？"
			},
			{
				"id": 49,
				"words": "你气不气？"
			},
			{
				"id": 48,
				"words": "打call"
			},
			{
				"id": 47,
				"words": "囍"
			},
			{
				"id": 44,
				"words": "还有这种操作！"
			},
			{
				"id": 39,
				"words": "请大家注意弹幕礼仪哦！"
			},
			{
				"id": 36,
				"words": "向大佬低头"
			},
			{
				"id": 25,
				"words": "prprpr"
			},
			{
				"id": 21,
				"words": "gg"
			},
			{
				"id": 20,
				"words": "你为什么这么熟练啊"
			},
			{
				"id": 19,
				"words": "老司机带带我"
			},
			{
				"id": 13,
				"words": "666666666"
			},
			{
				"id": 12,
				"words": "啪啪啪啪啪"
			},
			{
				"id": 11,
				"words": "Yooooooo"
			},
			{
				"id": 10,
				"words": "FFFFFFFFFF"
			},
			{
				"id": 7,
				"words": "红红火火恍恍惚惚"
			},
			{
				"id": 5,
				"words": "喂，妖妖零吗"
			},
			{
				"id": 2,
				"words": "2333333"
			}
		],
		"roomgifts": [
			{
				"id": 25,
				"name": "小电视",
				"price": 1245000,
				"type": 0,
				"coin_type": {
					"gold": "gold"
				},
				"img": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift-static-icon/gift-25.png?20180514161652",
				"gift_url": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift/2/25.gif?20180514161652",
				"count_set": "1,2,3,4",
				"combo_num": 1,
				"super_num": 1,
				"count_map": {
					"1": "高能",
					"2": "高能",
					"3": "高能",
					"4": "高能"
				}
			},
			{
				"id": 3,
				"name": "B坷垃",
				"price": 9900,
				"type": 0,
				"coin_type": {
					"gold": "gold"
				},
				"img": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift-static-icon/gift-3.png?20180514161652",
				"gift_url": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift/2/3.gif?20180514161652",
				"count_set": "1,10,46,520",
				"combo_num": 1,
				"super_num": 46,
				"count_map": {
					"1": "",
					"10": "",
					"46": "高能",
					"520": "高能"
				}
			},
			{
				"id": 4,
				"name": "喵娘",
				"price": 5200,
				"type": 0,
				"coin_type": {
					"gold": "gold"
				},
				"img": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift-static-icon/gift-4.png?20180514161652",
				"gift_url": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift/2/4.gif?20180514161652",
				"count_set": "1,10,87,520",
				"combo_num": 2,
				"super_num": 87,
				"count_map": {
					"1": "",
					"10": "",
					"87": "高能",
					"520": "高能"
				}
			},
			{
				"id": 6,
				"name": "亿圆",
				"price": 1000,
				"type": 0,
				"coin_type": {
					"gold": "gold"
				},
				"img": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift-static-icon/gift-6.png?20180514161652",
				"gift_url": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift/2/6.gif?20180514161652",
				"count_set": "1,10,450,1314",
				"combo_num": 10,
				"super_num": 450,
				"count_map": {
					"1": "",
					"10": "",
					"450": "高能",
					"1314": "高能"
				}
			},
			{
				"id": 7,
				"name": "666",
				"price": 666,
				"type": 1,
				"coin_type": {
					"gold": "gold"
				},
				"img": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift-static-icon/gift-7.png?20180514161652",
				"gift_url": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift/2/7.gif?20180514161652",
				"count_set": "1,2,3,4",
				"combo_num": 0,
				"super_num": 0,
				"count_map": {
					"1": "",
					"2": "",
					"3": "",
					"4": ""
				}
			},
			{
				"id": 8,
				"name": "233",
				"price": 233,
				"type": 1,
				"coin_type": {
					"gold": "gold"
				},
				"img": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift-static-icon/gift-8.png?20180514161652",
				"gift_url": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift/2/8.gif?20180514161652",
				"count_set": "1,2,3,4",
				"combo_num": 0,
				"super_num": 0,
				"count_map": {
					"1": "",
					"2": "",
					"3": "",
					"4": ""
				}
			},
			{
				"id": 1,
				"name": "辣条",
				"price": 100,
				"type": 0,
				"coin_type": {
					"silver": "silver"
				},
				"img": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift-static-icon/gift-1.png?20180514161652",
				"gift_url": "https://s1.hdslb.com/bfs/static/blive/live-assets/mobile/gift/mobilegift/2/1.gif?20180514161652",
				"count_set": "1,10,99,520",
				"combo_num": 0,
				"super_num": 0,
				"count_map": {
					"1": "",
					"10": "",
					"99": "",
					"520": ""
				}
			}
		],
		"ignore_gift": [
			{
				"id": 1,
				"num": 10
			},
			{
				"id": 21,
				"num": 10
			}
		],
		"msg_mode": 1,
		"msg_color": 16777215,
		"msg_length": 30,
		"master_level": 27,
		"master_level_color": 10512625,
		"broadcast_type": 0,
		"activity_gift": [],
		"check_version": 0,
		"activity_id": 0,
		"event_corner": [],
		"guard_level": 0,
		"guard_info": {
			"heart_status": 0,
			"heart_time": 300
		},
		"guard_notice": 0,
		"guard_tip_flag": 0,
		"new_year_ceremony": 0,
		"special_gift_gif": "https://static.hdslb.com/live-static/live-room/images/gift-section/mobilegift/2/jiezou.gif?2017011901",
		"show_room_id": 383045
	}
}
```



### 弹幕消息获取

URL：`https://api.live.bilibili.com/ajax/msg`

FORM：

```json
{
     "roomid": 383045,
     "csrf_token": "c93526e213231f715424af182dfb0411",
     "visit_id": ""
}
```

方法：`POST`

```json
{
	"code": 0,
	"data": {
		"admin": [],
		"room": [
			{
				"text": "哈哈哈",
				"nickname": "祁齐七",
				"uname_color": "",
				"uid": 13495205,
				"timeline": "2019-06-01 21:04:29",
				"isadmin": 0,
				"vip": 0,
				"svip": 0,
				"medal": [
					2,
					"酷唯",
					"DawningK鞠婧祎个站",
					867780,
					6406234,
					""
				],
				"title": [
					"",
					""
				],
				"user_level": [
					4,
					0,
					9868950,
					">50000"
				],
				"rank": 10000,
				"teamid": 0,
				"rnd": "-229520453",
				"user_title": "",
				"guard_level": 0,
				"bubble": 0,
				"check_info": {
					"ts": 1559394269,
					"ct": "E0A5D6C4"
				}
			},
			{
				"text": "哈哈",
				"nickname": "WULUOABC",
				"uname_color": "",
				"uid": 1293611,
				"timeline": "2019-06-01 21:04:30",
				"isadmin": 0,
				"vip": 0,
				"svip": 0,
				"medal": [],
				"title": [
					"",
					""
				],
				"user_level": [
					13,
					0,
					6406234,
					">50000"
				],
				"rank": 10000,
				"teamid": 0,
				"rnd": "1559393968",
				"user_title": "",
				"guard_level": 0,
				"bubble": 0,
				"check_info": {
					"ts": 1559394270,
					"ct": "34EE365B"
				}
			},
			{
				"text": "刚刚去了口袋，没人说话，我又回来了",
				"nickname": "鹅咕撒",
				"uname_color": "",
				"uid": 11561271,
				"timeline": "2019-06-01 21:04:30",
				"isadmin": 0,
				"vip": 0,
				"svip": 0,
				"medal": [],
				"title": [
					"",
					""
				],
				"user_level": [
					2,
					0,
					9868950,
					">50000"
				],
				"rank": 10000,
				"teamid": 0,
				"rnd": "1506254896",
				"user_title": "",
				"guard_level": 0,
				"bubble": 0,
				"check_info": {
					"ts": 1559394270,
					"ct": "D00B6637"
				}
			},
			{
				"text": "钻火圈",
				"nickname": "泠烙",
				"uname_color": "",
				"uid": 7764193,
				"timeline": "2019-06-01 21:04:31",
				"isadmin": 0,
				"vip": 0,
				"svip": 0,
				"medal": [],
				"title": [
					"",
					""
				],
				"user_level": [
					5,
					0,
					9868950,
					">50000"
				],
				"rank": 10000,
				"teamid": 0,
				"rnd": "1559392922",
				"user_title": "",
				"guard_level": 0,
				"bubble": 0,
				"check_info": {
					"ts": 1559394271,
					"ct": "3FE1FD97"
				}
			},
			{
				"text": "期待坨子当兵",
				"nickname": "悠唐四少",
				"uname_color": "",
				"uid": 23216713,
				"timeline": "2019-06-01 21:04:31",
				"isadmin": 0,
				"vip": 0,
				"svip": 0,
				"medal": [
					2,
					"超绝",
					"BEJ48",
					383045,
					6406234,
					""
				],
				"title": [
					"title-134-1",
					"title-134-1"
				],
				"user_level": [
					13,
					0,
					6406234,
					">50000"
				],
				"rank": 10000,
				"teamid": 0,
				"rnd": "1559389154",
				"user_title": "title-134-1",
				"guard_level": 0,
				"bubble": 0,
				"check_info": {
					"ts": 1559394271,
					"ct": "E1EDCE3E"
				}
			},
			{
				"text": "驼子当兵",
				"nickname": "嘿依呀哟",
				"uname_color": "",
				"uid": 12358754,
				"timeline": "2019-06-01 21:04:34",
				"isadmin": 0,
				"vip": 0,
				"svip": 0,
				"medal": [],
				"title": [
					"",
					""
				],
				"user_level": [
					1,
					0,
					9868950,
					">50000"
				],
				"rank": 10000,
				"teamid": 0,
				"rnd": "568573917",
				"user_title": "",
				"guard_level": 0,
				"bubble": 0,
				"check_info": {
					"ts": 1559394274,
					"ct": "8089A42F"
				}
			},
			{
				"text": "应该乐器类的吧",
				"nickname": "蔚蓝色的星晴",
				"uname_color": "",
				"uid": 46356206,
				"timeline": "2019-06-01 21:04:42",
				"isadmin": 0,
				"vip": 0,
				"svip": 0,
				"medal": [
					6,
					"聚聚",
					"SNH48官方账号",
					63727,
					5805790,
					""
				],
				"title": [
					"",
					""
				],
				"user_level": [
					18,
					0,
					6406234,
					">50000"
				],
				"rank": 10000,
				"teamid": 0,
				"rnd": "746908655",
				"user_title": "",
				"guard_level": 0,
				"bubble": 0,
				"check_info": {
					"ts": 1559394282,
					"ct": "8C0C6DF5"
				}
			},
			{
				"text": "我回家晚了。。。这是重播？",
				"nickname": "羽珩",
				"uname_color": "",
				"uid": 14987711,
				"timeline": "2019-06-01 21:04:42",
				"isadmin": 0,
				"vip": 0,
				"svip": 0,
				"medal": [],
				"title": [
					"",
					""
				],
				"user_level": [
					18,
					0,
					6406234,
					">50000"
				],
				"rank": 10000,
				"teamid": 0,
				"rnd": "1559394247",
				"user_title": "",
				"guard_level": 0,
				"bubble": 0,
				"check_info": {
					"ts": 1559394282,
					"ct": "3AE64C1F"
				}
			},
			{
				"text": "王雨兰~",
				"nickname": "嗯嗯嗯乖",
				"uname_color": "",
				"uid": 282579784,
				"timeline": "2019-06-01 21:04:42",
				"isadmin": 0,
				"vip": 0,
				"svip": 0,
				"medal": [],
				"title": [
					"",
					""
				],
				"user_level": [
					1,
					0,
					9868950,
					">50000"
				],
				"rank": 10000,
				"teamid": 0,
				"rnd": "-659981737",
				"user_title": "",
				"guard_level": 0,
				"bubble": 0,
				"check_info": {
					"ts": 1559394282,
					"ct": "B1D6EC27"
				}
			},
			{
				"text": "兰兰",
				"nickname": "静渡远洋",
				"uname_color": "",
				"uid": 30033220,
				"timeline": "2019-06-01 21:04:43",
				"isadmin": 0,
				"vip": 0,
				"svip": 0,
				"medal": [],
				"title": [
					"",
					""
				],
				"user_level": [
					15,
					0,
					6406234,
					">50000"
				],
				"rank": 10000,
				"teamid": 0,
				"rnd": "-1457418786",
				"user_title": "",
				"guard_level": 0,
				"bubble": 0,
				"check_info": {
					"ts": 1559394283,
					"ct": "D4155E7B"
				}
			}
		]
	},
	"message": "",
	"msg": ""
}
```



