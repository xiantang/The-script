def text_to_python_dir(text):
    dir={}
    words=text.split('\n')
    for word in  words:

        if word.startswith('    '):
            word=word.replace('    ','')
            word_item = word.split(' ',1)
            dir[word_item[0]]=word_item[1]
    print(dir)
if __name__ == '__main__':

    text='''abandon vt.丢弃；放弃,抛弃
    abandoned a. 被抛弃的；无约束的
    ability n.能力；能耐,本领
    able adj.有能力的；能干的
    about prep.关于；在…周围
    above prep.在…上面；高于
    abroad ad.(在)国外；到处
    absence n.缺席,不在场；缺乏
    absent a.不在场的；缺乏的
    absolute a.绝对的；纯粹的
    absolutely ad.完全地；绝对地
    absorb vt.吸收；使专心
    abuse vt.滥用；虐待 n.滥用
    academic a.学院的；学术的
    accent n.口音,腔调；重音
    accept vt.vi.接受；同意
    acceptable a.可接受的,合意的
    access n.接近；通道,入口
    accident n.意外的；事故
    accidental adj. 意外的,偶然的
    accidentally adv. 意外地,偶然地；偶尔,附带
    accommodation n.招待设备；预定铺位
    accompany vt.陪伴,陪同；伴随
    according ad. 根据
    account n.记述；解释；帐目
    accurate a.准确的,正确无误的
    accurately adj. 准确地；ad. 准确地；精密地
    accuse vt.指责；归咎于
    achieve vt.完成,实现；达到
    achievement n.完成；成就,成绩
    acid n.酸；酸的,酸性的
    acknowledge vt.承认；告知收到
    acquire vt.取得；获得；学到
    across prep.横过,穿过
    action n.行动；作用；功能
    active a.活跃的；积极的
    actively adv. 积极地,活跃地
    activity n.活动,能动性
    actor n.男演员；演剧的人
    actual a.实际的；现行的
    actually adv.实际上
    ad n. (缩)广告
    adapt vt.使适应；改编
    add vt.加,增加
    addition n.加,加法；附加物
    additional a.附加的,追加的
    address n.地址；演说；谈吐
    adequate a.足够的；可以胜任的
    adequately adv. 恰当地；足够地
    adjust vt.调整,调节；校正
    admiration n.羡慕,钦佩；赞赏
    admire vt.钦佩；羡慕；赞美
    admit vt.&vi.承认
    adopt vt.收养；采用；采取
    adult n.成年人 a.成年的
    advance vi.前进；提高 n.进展
    advanced a.先进的；高级的
    advantage n.优点,优势；好处
    adventure n.冒险,冒险活动
    advertise vt.通知 vi.登广告
    advertisement n.广告；公告；登广告
    advertising adj. 广告的；广告,广告费n. (总称)广告；
    advice n.劝告；忠告；意见
    advise vt. 忠告,劝告,建议；通知；告诉；通告
    affair n.事件；事情
    affect vt.影响；感动
    affection n.慈爱,爱；爱慕
    afford vt.担负得起…；提供
    afraid adj.(表语)怕,害怕
    after prep.在…以后；次于
    afternoon n.下午,午后
    afterwards ad. 以后,后来,然后
    again ad.又一次；而且
    against prep.反对；对着
    aged a. 年老的,经过相当岁月的,有...岁的
    agency n.经办；代理；代理处
    agent n.代理人,代理商
    aggressive a.侵略的；好斗的
    ago ad.以前
    agree vt.&vi.同意,赞成
    agreement n.协定,协议；同意
    ahead adv.在前面,在前头
    aid n.帮助,救护；助手
    aim n.瞄准；目标；目的
    air n.空气；空中；外观
    aircraft n.飞机,飞行器
    airport n.机场,航空站
    alarm n.惊恐,忧虑；警报
    alarming adj. 警告的；引起惊恐的
    alcohol n.酒精,乙醇
    alcoholic n. 酒鬼,酒精中毒的人
    alive adj.活着
    all adv.都
    allied a.联合的；联姻的
    allow vt.允许,准许；任
    ally n.同盟国；同盟者
    almost ad.几乎,差不多
    alone a.单独的 ad.单独地
    along prep.沿着 ad.向前
    alongside prep.在…旁边
    aloud ad.出声地,大声地
    alphabet n.字母表
    alphabetical adj.依字母顺序的
    alphabetically ad. 按字母表顺序
    already ad.早已,已经
    also ad.亦,也；而且,还
    alter vt.改变,变更；改做
    alternative n.替换物；取舍,抉择
    alternatively adv. 交互地；交替地；另外,此外；两者择一
    although conj.虽然
    altogether ad.完全；总而言之
    always adv.总是,一直
    amaze vt.使惊奇,使惊愕
    amazing adj. 惊人的；惊奇的；令人惊异的
    ambition n.雄心,抱负,野心
    ambulance n.救护车；野战医院
    among prep.在…之中
    amount n.总数；数量；和
    amuse vt.娱乐；逗...乐
    amusing adj. 令人感到有趣的；有趣的,逗人笑的；使人发笑的
    an art. 一(个,件,…)；(不定冠词,在元音前)；每一；任何一人；一个（本…）
    analyse vt.分析,分解,解析
    analysis n.分析,分解,解析
    ancient a.古代的,古老的
    and conj.和；又
    anger n.发怒
    angle n.角,角度
    angrily adv.发怒地,愤怒地
    angry adj.发怒的,生气的
    animal n.动物,兽 a.动物的
    ankle n.踝,踝节部
    anniversary n.周年纪念日
    announce vt.宣布,宣告,发表
    annoy vt.使恼怒；打搅
    annoying a. 恼人的,讨厌的；使人气恼的
    annual a.每年的 n.年报
    annually ad.一年一次,每年
    another adj.&pron.再一(个..)
    answer vt.回答；响应；适应
    anticipate vt.预料,预期,期望
    anxiety n.焦虑,忧虑；渴望
    anxious adj.渴望的；忧虑的
    anxiously adv. 焦急地,急切地；不安地；挂念地；渴望地；担心的
    any adj.什么,一些,任何的
    anyone pron.任何人
    anything pron.任何事(物)
    anyway ad.无论如何
    anywhere ad.在什么地方
    apart adv.分别；相距
    apartment n. 公寓；一套公寓房间；套房,(美)一套房间；房间,间；公寓住宅,套间
    apologize vi.道歉,谢罪,认错
    apparent a.表面上的；明显的
    apparently ad. 明显地；外表地；显然,表面上地；adj. 显然,似乎
    appeal vi.&n.呼吁；申述
    appear vi.出现；显得；好象
    appearance n.出现,来到；外观
    apple n.苹果
    application n.请求,申请；施用
    apply vt.应用,实施,使用
    appoint vt.任命,委任；约定
    appointment n.任命；约定,约会
    appreciate vt.感激；欣赏
    approach vt.向…靠近 n.靠近
    appropriate a.适当的,恰当的
    approval n.赞成,同意；批准
    approve vt.赞成,称许；批准
    approximate a.近似的 vt.近似
    approximately adv. 近乎,大约；近似地,几乎正确地；差不多
    April n.四月
    area n.地区
    argue vi.争论,争辩,辩论
    argument n.辩论；争论,论据
    arise vi.出现；由…引起
    arm n.手臂,胳膊
    arms n. 武器
    army n.军队
    around prep.在...周围
    arrange vt.整理,分类,排列
    arrangement n.整理,排列；安排
    arrest vt.逮捕,拘留；阻止
    arrival n.到达；到来；到达者
    arrive vi.到达；来临；达到
    arrow n.箭；箭状物
    art n.艺术；美术
    article n.文章,论文；冠词
    artificial a.人工的；娇揉造作的
    artificially ad. 人工地；假地；人造地
    artist n.美术家；艺术家
    artistic a.艺术的；艺术家的
    as conj.因为,由于
    ashamed a.惭愧(的)；羞耻(的)
    aside adv.在(到或向)旁边
    ask v.问
    asleep a.睡着的,睡熟的
    aspect n.方面；样子,外表
    assist vt.援助,帮助；搀扶
    assistance n. 协助,援助
    assistant n.助手,助理；助教
    associate vi.交往 n.伙伴,同事
    associated adj. 联合的；相联的adv. 副的
    association n.协会,团体；联合
    assume vt.假定；承担；呈现
    assure vt.使确信；向…保证
    at prep.在
    atmosphere n.大气；空气；气氛
    atom n.原子
    attach vt.缚,系,贴；附加
    attached a. 附加的
    attack vt.&vi.&n.攻击,进攻
    attempt vt.尝试,试图 n.企图
    attend vt.出席；照顾,护理
    attention n.注意,留心；注意力
    attitude n.态度,看法；姿势
    attorney n.代理人；辩护律师
    attract vt.吸引；引起,诱惑
    attraction n.吸引；吸引力；引力
    attractive a.有吸引力的
    audience n.听众,观众,读者
    August n.八月
    aunt n.伯母,婶母,姑母
    author n.创造者,创始人
    authority n.当局,官方；权力
    automatic a.自动的；机械的
    automatically ad. 自动地,机械地
    autumn n.秋,秋季
    available a.可利用的；通用的
    average n.平均数 a.平均的
    avoid vt.避免；回避,躲开
    awake vt.唤醒 vi.醒
    award n.奖,奖品；判定
    aware a.知道的,意识到的
    away ad.离开,远离；…去
    awful a.令人不愉快的
    awfully ad.令人畏惧的；很
    awkward a.笨拙的；尴尬的
    awkwardly ad. 局促不安地,笨拙地；a. 笨拙地；棘手地
    baby n.一家中年龄最小的人
    back adv.回(原处)；向后
    background n.背景,后景,经历
    backward a.向后的；倒的 ad.倒
    backwards ad. 向后
    bacteria n.细菌
    bad a.坏的,恶的；严重的
    badly adv.坏；恶劣地
    bad-tempered adj. 脾气坏的
    bag n.提包,口袋,书包
    baggage n.行李
    bake vt.烤,烘,焙；烧硬
    balance vt.使平衡；称 n.天平
    ball n.球
    ban n. 禁令
    band n.乐队；带；波段
    bandage n.绷带,包带
    bank n.银行；库；岩,堤
    bar n.酒吧间；条,杆；栅
    bargain n.交易 vi.议价；成交
    barrier n.栅栏,屏障；障碍
    base n.基础；基地,根据地
    basic a.基本的,基础的
    basically adv. 基本上,主要地；事实上；基本地
    basis n.基础,根据
    bath n.浴,洗澡；浴缸
    bathroom n.浴室；盥洗室
    battery n.炮兵连；兵器群
    battle vi.战斗 vt.与…作战
    bay n.海湾
    be aux.v.&vi.是,在,做
    beach n.海滩,湖滩,河滩
    beak n. 鸟嘴
    bear n.熊；粗鲁的人
    beard n.胡须,络腮胡子
    beat vt.&vi.打,敲；打败
    beautiful a.美的,美丽的
    beautifully ad. 美丽地；优美地
    beauty n.美；美人
    because conj.因为
    become vi.变成；成为,变得
    bed n.床
    bedroom n.卧室
    beef n.牛肉
    beer n.啤酒
    before prep.在…以前；向…
    begin vi.开始 vt.开始
    beginning n.开始,开端；起源
    behalf n.利益,维护,支持
    behave vi.表现,举止；运转
    behaviour n. 行为,举止；表现,(机器等的)运转达情况
    behind prep.在…后面
    belief n.相信；信念；信仰
    believe vt.相信；认为
    bell n.铃,钟
    belong vi.属于,附属
    below adv.在下面；向下
    belt n.带,腰带；皮带；区
    bend vt.使弯曲 vi.弯曲
    beneath prep.在…下方
    benefit n.利益；恩惠；津贴
    bent a. 弯曲的,决心的
    beside prep.在…旁边
    bet vt.&vi.&n.打赌
    better adj.较好的,(健康状况)好转的；更好的；adv. 更好地；较佳的；更多地；改进；较好；好些,更好些
    between prep.在…中间
    beyond prep.在…的那边
    bicycle n.脚踏车,自行车
    bid vt.命令 vi.报价
    big adj.大的
    bill n.账单；招贴；票据
    bin n. 箱柜
    biology n.生物学；生态学
    bird n.鸟,禽
    birth n.分娩；诞生；出身
    birthday n.生日
    biscuit n.(英)饼干；(美)软饼
    bit n.一点,一些
    bite vt.咬,叮,螫；剌穿
    bitter a.痛苦的；严寒的
    bitterly ad.苦苦地；悲痛地
    black adj.黑色的
    blade n.刀刃,刀片；叶片
    blame vt.责备,把…归咎于
    blank a.空白的 n.空白
    blind n.百叶窗；窗帘；遮帘
    block n.阻塞；障碍物；炮闩
    blonde a. n. 金发碧眼的（女子）
    blood n.血
    blow vt.&vi.吹
    blue adj. 蓝色的；伤心的；下流的；忧郁的；沮丧的,脸色发灰的n. 青色；蓝色
    board n.木板；板
    boat n.小船,艇；渔船
    body n.身体；主体；尸体
    boil vi.沸腾；汽化vt.煮沸
    bomb n. 炸弹；突发事件；高压喷雾器； vt. 投弹,轰炸；投弹于
    bone n.骨,骨骼
    book n.书,书籍 vt.预定
    boot n.靴子,长统靴
    border n.边,边缘；边界
    bore vt.令(人)厌烦
    boring n. 钻孔；adj. 讨厌的
    borrow vt.借
    boss n.老板,上司 vt.指挥
    both pron.两者(都)
    bother vt.烦扰,迷惑 n.麻烦
    bottle n.瓶,酒瓶；一瓶
    bottom n.底,底部,根基
    bound a.一定的；有义务的
    bowl n.碗
    box n.盒子
    boy n.男孩,少年；家伙
    boyfriend n. 男朋友
    brain n.脑(子)；脑力,智能
    branch n.枝条；支流；部门
    brand n.商品；烙印 vt.铭刻
    brave a.勇敢的,华丽的
    bread n.面包
    break n.(课间)休息时间
    breakfast n.早饭,早餐
    breast n.胸膛,胸部
    breath n.呼吸；气息
    breathe vi.&vt.呼吸
    breed n.(动物)品种
    brick n.砖,砖块；砖状物
    bridge n.桥,桥梁；桥牌
    brief a.简短的；短暂的
    briefly adv. 简单地,简短地；短暂地；简略地；简要地
    bright a.明亮的；聪明的
    brightly adv. 闪烁地；灿烂地；明亮地；聪明地
    brilliant a.光辉的；卓越的
    bring vt.带来；引出；促使
    broad adj.宽的；广阔的
    broadcast n.广播,播音
    broadly ad. 广,宽；明白；粗鲁
    broken a.被打碎的,骨折的
    brother n.兄,弟
    brown adj.褐色的,棕色的
    brush n.刷子,毛刷；画笔
    bubble n.泡 vi.冒泡,沸腾
    budget n.预算,预算案
    build vt.建筑；建立；创立
    building n.建筑物,大楼；建筑
    bullet n.子弹,枪弹
    bunch n.束,球,串；一群
    burn vi.&vt.燃烧
    burnt adj. 烧焦的,烧坏的；burn的过去式(分词)；燃烧(burnt=burned)
    burst n.突然破裂；爆发
    bury vt.埋葬,葬；埋藏
    bus n. 公共汽车；总线,信息通路
    bush n.灌木,灌木丛,矮树
    business n.商业,生意；事务
    businessman n. 商人,实业家
    busy adj.忙的；繁忙的
    but conj.但是,可是
    butter n.黄油；奶油
    button n.扣子；按钮 vt.扣紧
    buy vt.买
    buyer n. 买主,买方
    by prep.被,由
    bye int. ((口语))再见
    cabinet n.橱,柜；内阁
    cable n.海底电报
    cake n.蛋糕,饼,糕
    calculate vt.计算；估	计；计划
    calculation n.计算,计算结果
    call vt.把…叫做；叫,喊
    calm adj. 	平 静的；沉着的
    calmly adv. 平静地；沉着地；无风浪地；镇静地
    camera n.照相机
    camp n.野营,营地,兵营
    campaign n.战役；运动
    camping n. 野营
    can n.罐头,听头
    cancel vt.取消,撤消；删去
    cancer n.癌,癌症,肿瘤
    candidate n. 候选人
    candy n.糖果；砂糖结晶
    cannot can的否定式
    cap n.帽子
    capable a.有能力的,有才能的
    capacity n.容量；能力；能量
    capital n.资本,资金；首都
    captain n.陆军上尉；队长
    capture vt.捕获,俘获；夺得
    car n. 汽车；小卧车；(这里指)运货马车；轿车；电车；车,火车车厢
    card n.卡片；名片
    cardboard n. 厚纸板
    care n.照料；保护；小心
    career n.生涯,职业,经历
    careful a.仔细的；细致的
    carefully adv. 小心地；仔细地；注意地
    careless adj.粗心的
    carelessly adv. 粗心地；毫不在乎地；随便地,疏忽地
    carpet n.毛毯；地毯
    carrot n.胡罗卜
    carry vt. 拿；搬；带；提；扛,挑,刊登；搬动；带去；运送,携带；运载；传送；领,抱背,传播,输送；手提,肩挑；举动；进位,担负；vi. 抬,扛,搬运
    case n.情况；事实；病例
    cash n.现金,现款
    cast vt.投,扔,抛；浇铸
    castle n.城堡；巨大建筑物
    cat n.猫,猫科,猫皮
    catch vi.钩住；挂住；绊住
    category n.种类,类目；范畴
    cause n.原因,理由；事业
    cease vi.&vi.&n.停止,停息
    ceiling n.天花板；顶逢
    celebrate vt.庆祝；歌颂,赞美
    celebration n.庆祝；庆祝会
    cell n.细胞；小房间
    cent n.分
    centimetre n.公分,厘米
    central a.中心的；主要的
    centre n. 中心；中央；中枢；核心；vt. 集中；使集中,把…放在中部vi. 居中
    century n.世纪；百年
    ceremony n.典礼,仪式；礼节
    certain a.确实的；肯定的
    certainly ad.一定,必定；当然
    certificate n.证书,证件,执照
    chain n.链,链条,项圈
    chair n. 椅子；大学的讲座；(会议的)主席；vt. 当…的主席,主持
    chairman n.主席；议长,会长
    challenge n.挑战；要求,需要
    chamber n.会议室；房间；腔
    chance n.机会
    change n.零钱；找头 vt.兑换
    channel n.海峡；渠道；频道
    chapter n.章,回,篇
    character n.性格；特性；角色
    characteristic a.特有的 n.特性
    charge n. 主管；电荷；负责；责任；管理；费用；负荷；充电；使承担；看管；保管；代价；(pl. )费用,罪名；收费, vt. 罚款,指控；索价；装满；职责；索费；充电
    charity n.施舍；慈善事业
    chart n.图,图表；海图
    chase n.追逐,追赶,追求
    chat n. 聊天；闲谈； vi. 聊天；谈天；闲谈vt. 亲谈,
    cheap adj.廉价的,便宜的
    cheaply adv.廉价地；粗俗地；便宜地
    cheat vt.骗取；哄 vi.行骗
    check n.支票
    cheek n.面颊,脸蛋
    cheerful adj.高兴的；爽快的
    cheerfully ad. 高兴地；愉快地
    cheese n.乳酪,干酪
    chemical adj.化学的
    chemist n.化学家；药剂师
    chemistry n. 化学
    cheque n.支票
    chest n.胸部
    chew vt.咀嚼,嚼碎
    chicken n.鸡肉；小鸡
    chief n.首长,头子
    child n.小孩
    chin n.颏,下巴
    chip n.薄片,碎片
    chocolate n.巧克力；巧克力糖
    choice n.选择
    choose vt.&vi.选择
    chop vt.&vi.砍,伐
    church n.教堂
    cigarette n. 香烟,纸烟
    cinema n.电影院；电影,影片
    circle vt.环绕,盘旋 n.圆
    circumstance n.情况,条件；境遇
    citizen n.公民；市民,居民
    city n.城市,都市
    civil a.公民的；文职的
    claim n.权利,所有权
    clap n.拍手喝采声；霹雳声
    class n. (学校里的)班；课；阶级；同学们；班级；种类,等级；阶层；(一堂)课,门类,vt. 分类；班级,阶级；类别,把…分成等级
    classic n.名著 a.不朽的
    classroom n.教室
    clean a.清洁的；纯洁的
    clear adj. 晴朗的；清楚的；清澈的；清晰的；vt. & vt. 清除；扫除；清出(空地)；越过,使清澈；使清楚
    clearly adv. 清楚地；无疑地,清澈地；明白地,清晰地；明亮地
    clerk n.办事员；秘书
    clever adj.机灵的,聪明的
    click n.卡嗒声
    client n.顾客；诉讼委托人
    climate n.气候；风土,地带
    climb v.爬；攀登
    clock n.钟,仪表
    close v.关
    closed adj. 关着的；关闭的,停业的；闭迹
    closely adv. 细细地；紧密地,接近地；严密地；准确地；a. 精密地,仔细地
    closet n.壁橱；小房间
    cloth n.布；布料
    clothes n.衣服,服装；被褥
    clothing n.衣服,被褥
    cloud n.云
    club n.俱乐部；社团
    coach vt.辅导,指导,训练
    coal n.煤,煤块
    coast n.海岸,海滨(地区)
    coat n.外套,上衣；表皮
    code n.准则；法典；代码
    coffee n.咖啡
    coin n.硬币；铸造(硬币)
    cold a.冷的；冷淡的 n.冷
    coldly adv. 冷淡地；无情地
    collapse vi.倒坍；崩溃,瓦解
    colleague n.同事,同僚
    collect vt.收集 vi.收款
    collection n.搜集,收集；收藏品
    college n.(综合大学中的)学院
    colour n.颜色
    coloured a.有色的,着色的
    column n.柱,支柱,圆柱
    combination n.结合,联合；化合
    combine vt.使结合；兼有
    come vi.来,来到；出现
    comedy n.喜剧；喜剧场面
    comfort n.舒适；安慰 vt.安慰
    comfortable a.舒适的,安慰的
    comfortably adv. 舒适地
    command vt.命令,指挥；控制
    comment n.评论,意见；注释
    commercial a.商业的；商品化的
    commission n.委托,委任；委托状
    commit vt.犯(错误);干(坏事)
    commitment n. 约束；责任；承诺,约定
    committee n.委员会；全体委员
    common adj.普通的,一般地
    commonly ad.普通地,一般地
    communicate vi.&vt.通信；通话
    communication n.通讯；传达；交通
    community n.社区；社会；公社
    company n.公司
    compare vt.比较,对照；比作
    comparison n.比较,对照；比似
    compete vi.比赛；竞争；对抗
    competition n.竞争,比赛
    competitive a.竞争的,比赛的
    complain vi.抱怨,拆苦；控告
    complaint n.疾病,病痛；主诉
    complete adj.完全的,彻底的
    completely adv.完全地,彻底地
    complex a.结合的；复杂的
    complicate vt.使复杂；使陷入
    complicated v. 使复杂化,使混乱；adj. 难懂的,难解的；复杂的
    computer n.计算机,电脑
    concentrate vt.&vi.浓缩,提浓
    concentration n.集中；专注；浓缩
    concept n.概念,观念,设想
    concern n.关心,挂念；关系
    concerned a. 关心的
    concerning prep.关于
    concert n.音乐会；演奏会
    conclude vt.&vi.推断出,断定
    conclusion n.结论,推论；结尾
    concrete n.混凝土；具体物
    condition n.条件；状况
    conduct n.举止,行为；指导
    conference n.会议,讨论会
    confidence n.私房话,秘密,机密
    confident n.确信的,自信的
    confidently ad. 自信地；有信心地
    confine vt.限制；禁闭
    confirm vt.证实,肯定；批准
    conflict n.争论；冲突；斗争
    confront vt.使面对；使对证
    confuse vt.使混乱,混淆
    confusion n.混乱；骚乱；混淆
    congress n.大会；国会,议会
    connect vt.连接,连结；联系
    connection n.连接,联系；连贯性
    conscious a.意识到的；有意的
    consequence n.结果,后果
    conservative a.保守的 n.保守的人
    consider vt.考虑；把...看作
    considerable a.相当大的；重要的
    considerably ad. 十分地；相当地
    consideration n. 考虑,思考；体贴；照顾；原因；体谅；研究,讨论；补偿,报酬；理由；需考虑到的事,关心
    consist vi.由…组成；在于
    constant a.经常的；永恒的
    constantly adv. 经常地；不断地；不变地,a. 经常地
    construct vt.建造；建设；构筑
    construction n. 建设(不可数名词)；建造；建筑；建筑物；结构；作图(法)；修建；解释,工程；构造
    consult vt.查阅
    consumer n.消费者,用户
    contact vt.使接触；与…联系
    contain vt.包含,容纳；等于
    container n.容器；集装箱
    contemporary a.当代的,同时代的
    content n.内容,目录；容量
    contest vt.争夺,争取；辩驳
    context n.上下文；来龙去脉
    continent n.大陆；洲
    continue vt.继续,连续；延伸
    continuous adj. 连续的；持续的；连续不断的,不断的；延长的；不间断的
    continuously adv.连续不断地；连续地,持续地
    contract n.契约,合同；婚约
    contrast n. 对照；悬殊差别；对比；反差,对比度；vt. 使对比； 使与…对比；使与…对照 vi. 形成对比；对比(着重于相异处)
    contribute vt.捐献,捐助；投稿
    contribution n. 贡献
    control vt.&n.控制；支配
    controlled a. 受控制的,受操纵的
    convenient a.便利的；近便的
    convention n. 习俗,惯例；公约,(换俘等)协定；会议；常规,契约
    conventional a.普通的；习惯的
    conversation n.会话,非正式会谈
    convert v. 转变,改变,变换；使转变；使改变；变更；转换,改变信仰；n. 改变信仰者
    convince vt.使确信,使信服
    cook vi.烹调,煮 n.厨师
    cooker n. 炊具,厨师
    cookie n.小甜饼
    cooking n. 烹饪；烹调用的
    cool vi.&vt.(使)凉快,冷却
    cope vi.对付,应付
    copy vt.抄写 n.副本
    core n.果实的心,核心
    corner n.角；(街道)拐角
    correct a.正确的 vt.纠正
    correctly adv. 正确地；恰当地；adj. 正确地；恰当地
    cost vi.值(多少钱) n.成本
    cottage n.村舍,小屋
    cotton n.棉；棉线；棉布
    cough n. & v. 咳嗽；咳
    could aux.v.(can的过去式)
    council n.理事会,委员会
    count vt.数；计数
    counter n.柜台
    country n.国家,国土；农村
    countryside n.乡下,农村
    county n.英国的郡,美国的县
    couple n.一对；夫妇
    courage n.勇气,胆量,胆识
    course n.课程；过程；一道菜
    court n.法院,法庭；庭院
    cousin n.堂(或表)兄弟(姐妹)
    cover vt.盖,包括 n.盖子
    covered adj. 覆盖的
    covering n. 覆盖(物)；套,罩；adj. 包括的
    cow n.母牛,奶牛
    crack n.裂缝,裂纹 vi.爆裂
    cracked adj. 有裂缝的；碎的；粗哑
    craft n.工艺；手艺,行业
    crash n. (树倒下的)哗啦声；碰撞；坠毁；轰隆声,撞击声；起重机,鹤vi. 碰撞,坠落；撞坏,摔坏,砸碎；撞碎；v.破裂,爆裂；发出爆裂声；坠落,坠毁
    crazy a.疯狂的,荒唐的
    cream n.奶油,乳脂；奶油色
    create vt.创造；引起,产生
    creature n.生物,动物,家畜
    credit n.信用贷款；信用
    crime n.罪,罪行；犯罪
    criminal n.犯人,罪犯,刑事犯
    crisis n.危机；存亡之际
    crisp a.脆的；卷曲的
    criterion n.标准,准则,尺度
    critical a.决定性的；批评的
    criticism n.批评；批判；评论
    criticize vt.&vi.批评；责备
    crop n.庄稼；收成
    cross n.十字架 vt.&vi.穿过
    crowd n.群；大众；一伙人
    crowded adj. 拥挤；充(拥)满了的；拥挤的n. 拥挤的,密集的
    crown n.王冠,冕；花冠
    crucial a. 至关重要的
    cruel a.残忍的,残酷的
    crush vt.压碎,碾碎；镇压
    cry vi.哭；叫喊
    cultural adj.文化上的；文化的
    culture n.文化,文明；教养
    cup vt.使成杯形
    cupboard n.碗柜,碗碟橱；食橱
    curb n. 马勒；勒马链条；路边；路的边栏；抑制物；v.束缚；抑制；控制,制止,抑制场外交易
    cure vt.医治；消除 n.治愈
    curious adj.稀奇的,奇妙的
    curiously adv. 好奇地；稀奇古怪地
    curl vt.&vi.卷曲 n.卷发
    curly a.卷曲的；有卷毛的
    current a.当前的；通用的
    currently adv. 当前,广泛地；目前,普遍地；现在
    curtain n.(窗、门)帘；幕
    curve n.曲线；弯 vt.弄弯
    custom n.习惯,风俗；海关
    customer n.顾客,主顾
    customs a. 海关的；定做的(衣)；n. 海关；关税；关税进口税海关；进口税
    cut vt.切；割；砍
    cycle n.自行车,循环
    dad n.(口语)爸爸,爹爹
    daily a.每日的 n.日报
    damage vt.损害,毁坏 n.损害
    damp a.潮湿的,有湿气的
    dance vi.跳舞；摇晃 n.舞
    dancer n.舞者; 舞女;  (专业的) 舞蹈家
    dancing n. 舞蹈
    danger n.危险
    dangerous adj.危险的
    dare v.aux.敢；敢于
    dark adj.黑暗的
    data n.数据; 资料
    date n.日期
    daughter n.女儿
    day n.(一)天,白昼,白天
    dead adj.死的
    deaf adj.聋的
    deal vi.做买卖；对付
    dear adj.昂贵的,高价的
    death n.死,死亡；灭亡
    debate n.,vt.&vi.争论；辩论
    debt n.债,债务,欠债
    decade n.十年,十年期
    decay vt.使腐朽,使腐烂
    December n.十二月
    decide vi.&vt.下决心；决定
    decision n. 决定,决心；果断；判决,决议；判定,决策；决断
    declare vt.断言；声明；表明
    decline vt.下倾；偏斜；衰退
    decorate vt.装饰,装璜,修饰
    decoration n. 装饰,装饰品
    decorative a.装饰的；可作装饰的
    decrease v. 减少,降低,缩短；减小；减弱；n. 减少,减小
    deep adj.深的
    deeply adv. 深深地；深切地
    defeat n.击败；失败
    defence n.防御；防务；辩护
    defend vt.保卫,防守
    define vt.给…下定义；限定
    definite a.明确的；肯定的
    definitely adv. 一定,肯定地；一定地,明确地；绝对
    definition n. 定义,解说；释义；定界；解释；限定；明确；确实,清晰度；界限；(轮廓等)清晰,规定
    degree n.程度；度；学位
    delay vt.推迟；耽搁；延误
    deliberate a.深思熟虑的；审慎的
    deliberately adv.仔细考虑地,故意地；审慎地,慎重地；从容地；有意地
    delicate a.纤细的；易碎的
    delight n.快乐
    delighted adj. 大喜；高兴的,欣喜的；喜欢的
    deliver vt.投递,送交；发表
    delivery n. 投递；交付；分娩；递送,讲述；送交；交货；传送；交货,发送,传递
    demand vt. 要求；需要；询问；查问；v. 请求；查问；需要；n. 需要；请求,需求
    demonstrate vt.说明；论证；表露
    dentist n.牙科医生
    deny vt.否定；拒绝相信
    department n.部,司,局,处,系
    departure n.离开,出发,起程
    depend vi.依靠
    deposit vt.使沉淀；存放
    depress vt.使沮丧；按下
    depressed adj. 郁郁不乐；情绪低落的；消沉的；萧条的
    depth n.深度；深厚；深处
    derive vt. 取得；得到；来自；由来；(from)导出；起源于；追寻…的起源,派生,引出；vi. 起源；由来,衍生
    describe vt.形容；描写,描绘
    description n.描写,形容；种类
    desert vt.遗弃；擅离(职守)
    deserted adj. 被人遗弃的；废弃的,荒无的；无人的；无人居住的
    deserve vt.应受,值得
    design vt.设计 n.设计；图样
    desire vt.相望；要求 n.愿望
    desk n.书桌,办公桌
    desperate adj. 什么也不顾的；拼死的；绝望的；不顾一切的；危急的；令人绝望的
    desperately adv.绝望地,孤注一掷地；拼命地；令人绝望地
    despite prep. 尽管；不管,不顾；任凭；n. 轻蔑
    destroy vt.破坏；消灭；打破
    destruction n.破坏,毁灭,消灭
    detail n. 细节；枝节；零件；琐碎,小事；详细情况；元件,详情；详述；琐事vt. 详述,细说；详细说明
    detailed adj. 详细的,详尽的；说细的
    determination n.决心；决定；确定
    determine vt.决定；查明；决心
    determined adj. 坚决的,有决心的；确定的；毅然的
    develop vt.使(颜色等)显现
    development n. 发展；开发；生长；进展,显影；研制
    device n.器械,装置；设计
    devote vt.将…奉献,致力于
    devoted adj. 忠实的；热心的；献身于…的
    diagram n.图解,图表,简图
    diamond n.金钢石,钻石；菱形
    diary n.日记,日记簿
    dictionary n.词典,字典
    die vi.死
    diet n.饮食,食物
    difference n.差别；差；分歧
    different adj. 不同的
    differently adv. 不同地；有差别地
    difficult a.困难的；难对付的
    difficulty a.困难；难事；困境
    dinner n.正餐(午饭或晚饭)
    direct vt.指导
    direction n.方向,方位；指导
    directly ad.直接地；立即
    director n.指导者；理事；导演
    dirt n.尘,土；污物,污垢
    dirty a.脏的；下流的
    disabled adj. 残废的；禁止的,报废的；n. 残疾人
    disadvantage n.不利,不利地位
    disagree vi.意见不同；不一致
    disagreement n.不一致；争论
    disappear vi.消失,消散
    disappoint vt.使失望,使受挫折
    disappointed adj. 失望的；扫兴的
    disappointing a. 令人失望的
    disappointment n.失望；沮丧
    disapproval n.不赞成；不满意
    disapprove vt.vi. 不赞成
    disaster n.灾难,祸害；天灾
    disc n. 圆盘,唱片
    discipline n.纪律；训练 vt.训练
    discount n.折扣；打折扣卖
    discover vt.发现；暴露,显示
    discovery n.发现；被发现的事物
    discuss vt.讨论,谈论；论述
    discussion n.讨论,谈论；论述
    disease n.疾病
    disgust n.厌恶,憎恶
    disgusting a. 令人作呕的；使人讨厌的
    dish n.盘,碟；一道菜
    dishonest a. 不诚实的
    disk n.圆盘,唱片；磁盘
    dislike vt.&n.不喜爱,厌恶
    dismiss vt.打发走；开除
    display vt.陈列,展览；显示
    dissolve vt.解除(婚约等)
    distance n.距离；远处
    distinguish vt.区别,辨别,认别
    distribute vt.分发,分送；分布
    distribution n.分发,分配；分布
    district n.区,行政区；地区
    disturb vt.打扰,扰乱；弄乱
    disturbing a. 令人不安的；令人担心的
    divide vt.分；分配；分开
    division n.分,分配；除法
    divorce n.离婚,离异 vi.离婚
    do v.做
    doctor n.医生,医师；博士
    document n.公文,文件；证件
    dollar n.元(美国货币单位)
    domestic a.本国的；家庭的
    dominate vt.统治,支配,控制
    door n.门
    double adj.两倍的；双的
    doubt n.怀疑；疑虑 vt.怀疑
    down ad.向下,在下面
    downstairs adv.往楼下adj.楼下的
    downward adv.向下；...以下
    downwards adv. 向下,以下
    dozen n.一打,十二个
    draft n.草稿；汇票 vt.起草
    drag vt.拖,拉；拖曳
    drama n.一出戏剧,剧本
    dramatic a.引人注目的,戏剧的
    dramatically ad. 戏剧性地；显著地
    draw vt.&vi.拉；牵；引出
    drawer n.抽屉
    drawing n.图画,素描；绘图
    dream vt.&vi.做梦 n.梦想
    dress n.衣服；连衣裙
    drink vt.饮 vi.喝 n.饮料
    drive vt.&vi.驱赶；驾驶
    driver n.驾驶员,司机
    drop vt.使落下；降低
    drug n.药,药物,药材
    drugstore n. (美国习俗)杂货店；零食店
    drum n.鼓；鼓状物,圆桶
    drunk a.醉的；陶醉的
    dry vt.使干 vi.变干
    due a.预期的；应给的
    dull a.枯燥的；不鲜明的
    dump vt.倾卸,倾倒；倾销
    during prep.在...的期间
    dust n.垃圾,废品,灰烬
    duty n.义务；责任
    dying a.垂死的；临终的
    each pron.各,各自 a.各
    ear n.耳朵；听力,听觉
    early adv.早
    earn vt.赚得,挣得；获得
    earth n.地球
    ease n.安逸,熟练,轻易
    easily ad.容易地；舒适的
    east n.东,东方 adj.东方的
    eastern a.东方的；朝东的
    easy adj.容易
    eat vt.吃,喝 vi.吃饭
    economic adj.经济的；经济学的
    economy n.经济；节约,节省
    edge n.边缘；边
    edition n.版,版本,版次
    editor n.编辑,编者,校订者
    educate vt.教育；培养；训练
    educated adj. 受过教育的
    education n.教育；训导；教育学
    effect n.结果；影响；效果
    effective a.有效的；有影响的
    effectively adv. 有效地
    efficient a.效率高的,有能力的
    efficiently ad. 有效地；能胜任地
    effort n.努力；努力的成果
    egg n.蛋
    either conj.或者, 要么
    elbow vt.用肘挤,挤进
    elderly a. 过了中年的,稍老的
    elect vt.选举,推选；选择
    election n.选举,选择权；当选
    electric a.电的,电动的
    electrical a.电的,电气科学的
    electricity n.电,电学；电流
    electronic a.电子的
    elegant a.(举止、服饰)雅致的
    element n.元素；要素；成分
    elevator n.电梯；升降机
    else adj.别的 adv.另外
    elsewhere ad.在别处,向别处
    email n.电子邮件
    embarrass vt.使负债；使复杂化
    embarrassed a. 窘迫,尴尬
    embarrassing adj. 令人为难的；令人尴尬的
    embarrassment n. 困难,阻碍,困窘
    emerge vi.出现,涌现；冒出
    emergency n.紧急情况,突然事件
    emotion n.感情；情绪；激动
    emotional a.感情的,情绪的
    emotionally ad. 感情上
    emphasis n.强调,重点,重要性
    emphasize vt.强调,着重
    empire n.帝国
    employ vi.雇用；用；使忙于
    employee n.受雇者,雇员,雇工
    employer n.雇佣者,雇主
    employment n.工业；雇用；使用
    empty a.空的；空洞的
    enable vt.使能够,使可能
    encounter vt.遭遇,遇到 n.遭遇
    encourage vt.鼓励,支持,助长
    encouragement n. 鼓励,激励,奖励
    end n.目标,目的
    ending n.结尾,结局；死亡
    enemy n.敌人；仇敌；敌兵
    energy n.活力；精力；能
    engage vt.使从事于；聘用
    engaged adj. 占用的,从事…的
    engine n.发动机,引擎；机车
    engineer n.工程师,技师
    engineering n.工程,工程学
    enjoy vt.享受；欣赏,喜爱
    enjoyable a. 可享受的,令人愉快的
    enjoyment n.享乐；欣赏
    enormous a.巨大的,庞大的
    enough adj.足够的adv.充分地
    enquiry v. 询问
    ensure vt.保证；保护；赋予
    enter vt.走进,进入；参加
    entertain vt.使欢乐；招待
    entertaining a. 有趣的
    entertainment n.招待,招待会
    enthusiasm n.热情,热心,热忱
    enthusiastic a.热情的,热心的
    entire a.全部的,整个的
    entirely adv.完全地；彻底地
    entitle vt.把…称作
    entrance n.入口；进入；入场
    entry n.入口处；登记；进入
    envelope n.信封
    environment n.环境,外界；围绕
    environmental adj. 环境的；环境产生的；周围的
    equal a.相等的；平等的
    equally adv. 相等地,相同地；同样；平等地；同样地
    equipment n.装备；设备
    equivalent a.相等的；等量的
    error n.错误,谬误；差错
    escape n.&vi.逃跑
    especially ad.特别,尤其,格外
    essay n.短文,散文,小品文
    essential a.必要的,本质的
    essentially adj. 本质上,实质上；ad. 本质上,基本上；实质上,本来
    establish vt.建立,设立；确立
    estate n.房地产；财产,产业
    estimate vt.估计,评价 n.估计
    even adv.甚至,即使
    evening n.傍晚,晚上
    event n.事件,大事；事变
    eventually ad.终于；最后
    ever adv.曾经
    every adj.每一,每个的
    everyone pron.每人,人人
    everything pron.每件事,每样东西
    everywhere adv.到处,无论哪里
    evidence n.根据；证据,证人
    evil adj.邪恶的 n.罪恶
    exact a.确切的；精确的
    exactly adv.确切地,恰恰正是
    exaggerate vt.&vi.夸大,夸张
    exaggerated adj. 言过其辞的
    exam n. (口语)考试；检查,细查；(exam＝examination)考试
    examination n.检查；考试
    examine vt.检查；诊察
    example n.例子；榜样
    excellent adj.极好的,优秀的
    except prep.除...之外
    exception n.例外,除外
    exchange vt.交换；交流 n.交换
    excite vt.使兴奋；使激动
    excited adj. 兴奋的；激昂的；激动的
    excitement n. 刺激,兴奋
    exciting adv. & adj. 激动人心的；adj. 令人兴奋的；令人激动的；使激动的；兴奋的；使人振奋的
    exclude vt.把…排除在外
    excuse n.藉口；托辞
    executive n.总经理,董事
    exercise n.练习
    exhibit vt.显示；陈列,展览
    exhibition n.展览
    exist vi.存在；生存
    existence n.存在,实在；生存
    exit n.出口；退场 vi.退出
    expand vt.扩大；使膨胀
    expect vt.料想,认为
    expectation n.期待,期望,预期
    expected a. 预期的,期待的
    expense n.消费；花费
    expensive adj.昂贵的
    experience n.经验,感受；经历
    experienced adj. 有经验的；老练的；熟练的
    experiment n.实验；试验
    expert n.专家 a.熟练的
    explain vt.&vi.解释,说明
    explanation n.解释,说明；辩解
    explode vt.使爆炸 vi.爆炸
    explore vt.&vi.探险,探索
    explosion n.爆炸,爆发,炸裂
    export vt.输出,出口；运走
    expose vt.使暴露；揭露
    express vt.表示 n.快车,快递
    expression n.词句；表达；表情
    extend vt.延长；扩大；致
    extension n.延长部分；伸展
    extensive a.广阔的；广泛的
    extent n.广度；范围；程度
    extra a.额外的 ad.特别地
    extraordinary a.非同寻常的,特别的
    extreme n.极端不同的性质
    extremely ad.极端,极其,非常
    eye n.眼睛；眼力；鉴赏力
    face n.脸
    facility n.设备；容易；便利
    fact n.事实；实际
    factor n.因素；因子,系数
    factory n.工厂,制造厂
    fail vi.失败
    failure n.失败；失败的人
    faint adj.暗淡的；微弱的
    faintly ad. 微微地；不明显的；微弱地,软弱无力的
    fair adj.(头发)金色的
    fairly ad.相当；公平地
    faith n.信任,信心；信仰
    faithful a.忠诚的；如实的
    faithfully adv. 忠诚地；诚恳地；忠实地
    fall n.&vi.落下；跌倒
    false a.不真实的；伪造的
    fame n.名声,名望
    familiar a.熟悉的；冒昧的
    family n.家,家庭
    famous adj.著名的
    fan n.扇子
    fancy n.想象力；设想；爱好
    far adj.远的 adv.远地
    farm n.农场
    farmer n.农民,农夫；农场主
    farming n. 农事；耕作；农业,种植业；耕作；n. & a. 农业(的)
    farther ad.更远地 a.更远的
    fashion n.样子,方式；风尚
    fashionable a.流行的,时髦的
    fast adv.快地 adj.快的
    fasten vt.&vi.扎牢；扣住
    fat adj.肥胖的
    father n.父亲
    faucet n. 水龙头
    fault n.缺点；过失；故障
    favour n.好感；赞同；恩惠
    favourite a.特别受喜爱的
    fear n.害怕；担心 vt.害怕
    feather n.羽毛；翎毛；羽状物
    feature n.特征,特色；面貌
    February n.二月
    federal a.联邦的；联盟的
    fee n.费,酬金；赏金
    feed vt.喂(养) vi.吃饲料
    feel vi.有知觉 vt.触,摸
    feeling n.感情；感觉,知觉
    fellow n.人,家伙；伙伴
    female n.雌性的动物；女子
    fence n.栅栏
    festival n.节日；音乐节
    fetch vt.拿来；请来,接去
    fever n.发热,发烧；狂热
    few a.很少的；少数的
    field n.地,田地
    fight vi.&vt.打仗(架)
    fighting a. 战斗的
    figure n.数字；外形；人物
    file n.档案 vt.把…归档
    fill vt.装满,盛满；占满
    film n.电影
    final a.最后的；决定性的
    finally ad.最后；不可更改的
    finance vt.提供资金
    financial a.财政的,金融的
    find v.找到；发现
    fine adj.好的 adv.很好,妙
    finely ad. 精细地,美好地
    finger n.手指
    finish vt.完成,结束 n.结束
    finished adj. 制成的；结束的；精致的；完成的
    fire n.火；火灾 vi.开火
    firm n.商行,商号,公司
    firmly adv. 紧紧地；坚定地；牢牢地；坚固地；稳定地；牢固地,断然地,固定地
    first num.第一
    fish n.鱼肉；鱼
    fishing n. 钓鱼,捕鱼；渔场；渔业
    fit vt.&vi.适合,合身
    fix vt.使固定；决定
    fixed adj.坚决的；固定的,已确定的；确定了的；不变的
    flag n.旗
    flame vi.发火焰 vt.点燃
    flash vi.(火焰等)一闪,闪亮
    flat a.平的,扁平的
    flavour n.味,味道；风味
    flesh n.肉；肉体
    flight n.航班；飞行；逃跑
    float vi.漂浮 vt.使漂浮
    flood n.洪水 vt.淹没
    floor n.地板；楼层
    flour n.面粉,粉；粉状物质
    flow vi.流,流动
    flower n.花,花卉；开花
    flu n.流行性感冒
    fly v.飞跑,逃跑,消失
    focus vi.聚焦,注视 n.焦点
    fold vt.折叠；合拢 n.褶
    follow vt.跟随;(时间等)接着
    following adj. 接着的；以下的；下列的；其次的；在…以后n. 下一个
    food n.食物
    foot n. 足；脚；英尺；最下部；底部
    football n.足球比赛；足球
    for prep.为
    force vt.强迫,迫使
    forecast n.预测,预报 vt.预示
    foreign adj. 外国的；外来的；无关的；对外的；外国来的；(to)使联系的；异质的,陌生的
    forest n.森林
    forever ad.永远,总是,老是
    forget vt.忘记,遗忘
    forgive vt.原谅,饶恕,宽恕
    fork n.叉；餐叉
    form vt.(使)组成,建立
    formal a.正式的；礼仪上的
    formally ad. 形式地,正式地；adj. 正式的
    former a.在前的 n.前者
    formerly ad.以前,从前
    formula n.公式,式
    fortune n.命运,运气；财产
    forward adv.向前,前进
    found vt.创立,创办；建立
    foundation n.地基
    frame n.框架,框子；构架
    free a.自由的；空闲的
    freedom n.自由；自主
    freely ad.自由地；直率地
    freeze vi.冻；结冻vt.使结冰
    frequent a.时常发生的；经常的
    frequently ad.时常,常常
    fresh adj.新鲜的
    freshly ad. 新近,刚才
    Friday n.星期五
    fridge n. 电冰箱
    friend n.朋友
    friendly adj.友好的
    friendship n.友谊,友好
    frighten vt.吓唬
    frightened adj. 受惊的,害怕的；受惊吓的
    frightening adj. 令人害怕的
    from prep.从；从...起；由
    front a.前面的 n.前部
    frozen freeze的过去分词；a. 冷冻的；冻结
    fruit n.水果
    fry vt.油煎,油炸,油炒
    fuel n.燃料 vt.给…加燃料
    full adj.满
    fully ad. 十分地,完全地
    fun n.有趣的事,玩笑
    function n.功能；职务；函数
    fund n.资金；基金；存款
    fundamental a.基础的,基本的
    funeral n.葬礼,丧礼,丧葬
    funny adj.滑稽可笑的
    fur n.(兽类的)软毛；皮毛
    furniture n.家具；装置,设备
    further vt.增进
    future n.将来,未来
    gain vt.&vi.获得 n.利益
    gallon n.加仑
    gamble n.赌博 vt.冒…的险
    gambling n. 赌博
    game n.游戏,运动,比赛
    gap n.空隙；缺口
    garage n.汽车间(或库)
    garbage n.垃圾,污物,废料
    garden n.花园,菜园；公园
    gas n.煤气；气体；汽油
    gasoline n.(美)汽油
    gate n.大门
    gather vt.推测,推断
    gear n.齿轮,传动装置
    general a.总的；一般的n.将军
    generally ad.一般地；通常地
    generate vt.发生；引起；生殖
    generation n.一代,一代人；产生
    generous a.慷慨的；宽厚的
    gentle adj.柔和的
    gentleman n.绅士；有教养的人
    gently adv.温柔地；柔和地
    genuine a.真的；真正的
    genuinely ad. 由衷地
    geography n.地理,地理学
    get v.取
    giant n.巨人；巨物
    gift n.礼物,赠品；天赋
    girl n. 女孩；姑娘；女孩子,女儿；少女,女人；女职员
    girlfriend n. 女朋友
    give vt.做,作；送给
    glad a.高兴的；乐意的
    glass n.玻璃；玻璃杯
    global adj.球面的；全球的；全世界的,总的；世界的；地球的,环球的,全局的n. 全局,全程,全局符
    glove n.手套
    glue n.胶,胶水 vt.胶合
    go v.去
    goal n.球门；得分；目的
    god n.神,神像；上帝
    gold n. 金子；黄金；金黄色；金色；金；钱财,金币,财富；a. 金的；黄金的；金制的；金质；黄金,含金的
    good adj.好的
    goodbye int. 再见
    goods n.商品；货物
    govern vt.统治,治理；支配
    government n.政府；治理；政治
    governor n.统治者；总督
    grab vt.&vi.急抓；抢
    grade n.年级
    gradual a.逐渐的；渐进的
    gradually adv. 逐渐地；逐步地
    grain n.谷物,谷类；谷粒
    gram n. 克,绿豆
    grammar n.语法；语法书
    grand adj.庄严的；伟大的
    grandchild n. 孙子; 孙女; 外孙; 外孙女
    granddaughter n.孙女,外孙女
    grandfather n.祖父；外祖父
    grandmother n.祖母,外祖母
    grandparent n. 祖父或祖母,祖父母
    grandson n.孙子,外孙子
    grant n.授予物,拨款
    grass n.草；草地
    grateful a.可喜的,令人愉快的
    grave n.坟墓 a.严重的
    gray a.灰色的 n.灰色
    great adj.伟大的；重大的
    greatly ad.大大地,非常
    green adj.绿色的
    grey adj.灰色的
    groceries n. 食品(店)；杂货(店)
    grocery n.食品杂货店
    ground n.地；场地；根据
    group n.小组,群 vi.聚集
    grow vi.生长；变得；增长
    growth n.增长；增长量；生长
    guarantee n.保证；担保物
    guard n.哨兵,警卫员
    guess v.猜
    guest n.客人
    guide n.向导,导游者
    guilty a.内疚的；有罪的
    gun n.枪,炮,手枪
    guy n. （铁塔等的）支索,牵索
    habit n.习惯；习性
    hair n.头发
    hairdresser n. 理发师,美容师
    half n.半,一半
    hall n.会堂,大厅,礼堂
    hammer n.锤,榔头 vt.锤击
    hand n.手
    handle n.柄,把手 vt.拿,触
    hang vt.挂,悬；吊死
    happen vi.(偶然)发生
    happily ad. 幸福地,快乐地,幸好
    happiness n.幸福,幸运；快乐
    happy adj.高兴的,幸福的
    hard adj.困难的；硬的
    hardly ad.几乎不,简直不
    harm n.伤害,损害 vt.损害
    harmful a.有害的
    harmless adj.无害的
    hat n.帽子
    hate vt.恨,憎恨；不喜欢
    hatred n.憎恶,憎恨,仇恨
    have v.有
    he pron.(主格)他
    head n.头
    headache n.头痛；头痛的事
    heal vt.治愈；使和解
    health n.健康,健康状况
    healthy adj.健康的
    hear v.听见,听
    hearing n.听；听力
    heart n.心(脏)
    heat n.热,炎热 vi.变热
    heating n.加热,供暖
    heaven n.天堂；天,天空
    heavily ad.重重地；大量地
    heavy adj.重的
    heel n.脚后跟,踵,后跟
    height n.高,高度；高处
    hell n.地狱；极大的痛苦
    hello interj.喂,你好；哟!；喂；vt. & vi. 喂；你好
    help v.帮助,帮忙
    helpful a.给予帮助的；有用的
    hence ad.因此,所以；今后
    her pron.她的
    here adv.这儿
    hero n.男主角；英雄；勇士
    hers pron.她的(所有物)
    herself pron.她自己；她亲自
    hesitate vi.踌躇；犹豫
    hi interj.你好；喂(问候等)；嗨(表示问候等)
    hide n.生皮,兽皮,皮革
    high adv.高高地 adj.高的
    highlight n. 增强亮度,提示区；最重要的部分,最精彩的场面；vt. 使显著,使突出,着重
    highly adv. 高度地；非常；很,十分,赞许地
    highway n.公路；大路
    hill n.小山
    him pron.他(宾格)
    himself pron.他自己；他亲自
    hip n.臀部,髋；屋脊
    hire vt.租借 n.租用,雇用
    his pron.他的
    historical adj.有关历史的；历史(上)的；根据历史上的发展叙述的
    history n.历史,历史学
    hit vt.打；击中；撞
    hobby n.业余爱好,癖好
    hold vt.抓住；抑制
    hole n.洞；孔眼,裂开处
    holiday n.假日,节日；假期
    hollow a.空的；空洞的
    holy a.神圣的；圣洁的
    home adv.回家,在家 n.家
    homework n.家庭作业
    honest a.诚实的；可敬的
    honestly ad. 诚实地；老实地
    honour vt.给...以荣誉
    hook vt.用钩连接,用钩挂
    hope n.&vt.&vi.希望
    horizontal a.地平的；水平的
    horn n.喇叭
    horror n.恐怖；厌恶
    horse n.马
    hospital n.医院
    host n.主人；东道主
    hot a.热的；刺激的；辣的
    hotel n.旅馆
    hour n.小时；时间,时刻
    house n.房屋,住宅；商号
    household n.家庭,户；家务
    housing n. 住房供给,住房建筑,马衣,装饰
    how ad.怎么；怎样；多少
    however adv.可是,不过
    huge adj.巨大的
    human n.人 adj.人的,人类的
    humorous a.富于幽默的,诙谐的
    humour n. 幽默；诙谐,滑稽；情绪；幽默感；v. 纵容,迁就
    hungry a.饥饿的；渴望的
    hunt vi.打猎
    hunting n. 打猎；狩猎
    hurry vi.赶紧 vt.催促
    hurt vt.使受伤；使痛心
    husband n.丈夫
    I pron.(主格)我
    idea n.主意,念头,思想
    ideal a.理想的；观念的
    ideally ad. 理想地；理论上
    identify vt.认出,识别,鉴定
    identity n. 同一性；特性
    if conj.假如,如果
    ignore vt.不顾,不理,忽视
    ill adj.病的
    illegal a.不合法的,非法的
    illegally adj. 非法地
    illness n.病,疾病
    illustrate vt.(用图等)说明
    image n.像；形象；映象
    imaginary a.想象中的,假想的
    imagination n.想象；想象力；空想
    imagine vt.想象；设想
    immediate a.立即的；直接的
    immediately adv. 立即；直接地；立刻,马上；紧挨着地；即刻；立即地
    immoral adj. 不道德的,淫荡的
    impact n.影响,作用；冲击
    impatient a.不耐烦的,急躁的
    impatiently ad. 不耐烦地,急躁地
    implication n.含义,暗示,暗指
    imply vt.暗示,意指
    import vt.&n.输入,进口
    importance n.重要；重要性
    important a.重要的；有势力的
    impose vi.利用；欺骗
    impossible a.不可能的,办不到的
    impress vt.印;留下极深的印象
    impression n.印；印象；印记
    impressive a.给人印象深刻的
    improve vt.使更好 vi.改善
    improvement n.改进,改善；改进处
    in prep.在...里面
    inability n. 无能,无力
    inch n.英寸
    incident n.小事件；插曲；事变
    include vt.包括,包含
    including prep. 包括；包含
    income n.收入；收益；进款
    increase vt.&vi.&n.增加
    increasingly ad.日益,越来越多地
    indeed adv.的确；真正地
    independence n.独立,自主,自立
    independent a.独立的；自主的
    independently adv. 独立地；自由地；独自地,单独地；a. 独立地
    index n.索引；指数；指标
    indicate vt.标示,表示；表明
    indication n.指示；表示；表明
    indirect a.间接的；不坦率的
    indirectly adj. 间接地；迂回地
    individual a.特殊的
    indoor adj. 室内的；室内进行的；屋里的
    indoors adv.在屋里；进入室内
    industrial a.工业的；产业的
    industry n.工业,产业；勤劳
    inevitable a.不可避免的,必然的
    inevitably ad. 必然地；不可避免地；不可避免的
    infect vt.使受影响
    infection n. 传染,影响,传染病
    infectious a.传染的；感染性的
    influence n.势力,权势
    inform vt.通知,向…报告
    informal a. 非正式的,不拘礼的,通俗的
    information n.消息,信息；通知
    ingredient n.配料,成分
    initial a.词首的
    initially adv. 最初,开始；开头
    initiative a.创始的 n.第一步
    injure vt.伤害,损害,损伤
    injury n.损害,伤害；受伤处
    ink n.墨水,油墨
    inner a.内部的；内心的
    innocent a.清白的,幼稚的
    inquiry n.询问,打听；调查
    insect n.昆虫,虫
    insert vt.插入; 嵌入; 登载
    inside prep.在…里面 n.内部
    insist vi.坚持；坚持要求
    install vt.安装,设置
    instance n.例子,实例,事例
    instead adv.代替,顶替
    institute n.研究所；学院
    institution n.协会；制度,习俗
    instruction n.命令；教学；教训
    instrument n.仪器；工具；乐器
    insult vt.&n.侮辱,凌辱
    insurance n.保险；保险费
    intelligence n.智力；理解力；情报
    intelligent a.聪明的；理智的
    intend vt.想要,打算；意指
    intention n.意图,意向,目的
    interest vt.使发生兴趣 n.兴趣
    interested adj. 感兴趣的；关心的；有兴趣；关注的
    interesting a.有趣的,引人入胜的
    interior n.内部 a.内部的
    internal a.内的；国内的
    international a.国际的,世界(性)的
    Internet n.国际互连网
    interpret vt.解释,说明；口译
    interpretation n.解释；口译
    interrupt vt.打断(讲话)；打扰
    interruption n.中断,打断；障碍物
    interval n.间隔；休息；间距
    interview vt.采访
    into prep.进,入；进入到
    introduce vt.提出(议案等)
    introduction n.介绍；引进；引言
    invent vt.发明,创造
    invention n.发明,创造
    invest vt.投资；投入
    investigate vt.&vi.调查
    investigation n.调查,调查研究
    investment n.投资,投资额,投入
    invitation n.请帖；邀请
    invite vt.邀请,聘请；招待
    involve vt.使卷入；牵涉
    involved adj. 涉及的,复杂的；有关的；有密切关系的
    involvement n. 卷入,涉足
    iron n.铁；铁制品
    irritate vt.激怒；引起不愉快
    irritating a. 气人的
    island n.岛；岛状物
    issue n.问题；发行 vt.发行
    it pron.它
    item n.条,条款；一条
    its pron.它的
    itself pron.它自己；自身
    jacket n.短上衣,茄克衫
    jam n.堵塞 vt.使…堵塞
    January n.一月
    jealous a.妒忌的；猜疑的
    jeans n. 斜纹布裤子,牛仔裤；斜纹布,(pl.)工装裤
    jelly n.冻,果子冻；胶状物
    jewellery n.珠宝,珠宝饰物
    job n.工作
    join vt.加入
    joint n.接头,接缝；关节
    joke n.笑话 vi.说笑话
    journalist n.记者,新闻工作者
    journey n.旅行,旅程,路程
    joy n.欢乐；高兴
    judge n.法官
    judgement n.意见；审判；判断
    juice n.(水果等)汁,液
    July n.七月
    jump vi.跳；暴涨 vt.跳过
    June n.六月
    junior n.年少者；晚辈
    just adv.正好,恰好
    justice n.正义,公正；司法
    justified a. 正当的,合理的
    justify vt.证明…是正当的
    keen a.热心的；激烈的
    keep vi.保持；坚持
    key n.钥匙
    keyboard n.键盘
    kick vi.&vt.&n.踢
    kid n.小孩,儿童,少年
    kill vt.杀死
    kilogram n.千克,公斤
    kilometre n.千米,公里
    kind adj.仁慈的；和蔼的
    kindly a. 和蔼的,温和的,爽快的
    kindness n.仁慈,好意
    king n.国王,君主
    kiss n.&vt.吻 vi.接吻
    kitchen n.厨房,灶间
    knee n.膝,膝盖,膝关节
    knife n.小刀
    knit vt.把…编结 vi.编织
    knitting n. 编织(物)；接合；联合
    knock vi.敲；击,打
    knot n.(绳的)结,(树的)节
    know vt.知道；认识；通晓
    knowledge n.知识,学识；知道
    label n.标签；标记,符号
    laboratory n.实验室
    labour n.劳动
    lack n.,vi.&vt.缺乏,没有
    lacking a. 缺少的,没有的
    lady n.女士；有教养的妇女
    lake n.湖
    lamp n.灯
    land n.陆地
    landscape n.风景,景色,景致
    lane n.(乡间)小路；跑道
    language n.语言
    large adj.大的；巨大的
    largely ad.大部分；大量地
    last a.最后的 ad.最后
    late a.迟的 ad.迟,晚
    later adv. 以后,后来；更晚,；较晚；过一会儿；过后；a. 更后的,后面的；较迟的,较近
    latest a. 新近的
    latter a.(两者中)后者的
    laugh vi.笑,发笑 n.笑
    launch vt.发射;发动(战争等)
    law n.法律,法令
    lawyer n.律师；法学家
    lay vt.放,搁；下(蛋)
    layer n.层,层次；铺设者
    lazy adj.懒惰的
    lead vt.领导
    leader n.领袖；领导人
    leading a.指导的；最主要的
    leaf n.叶
    league n.联盟
    lean vi.倾斜,屈身；靠
    learn vi.&vt.学,学习
    least a.最少的 ad.最少
    leather n.皮革；皮革制品
    leave vt.离开;剩下 vi.离去
    lecture n.&vi.演讲,讲课
    left a.左边的 ad.在左边
    leg n.腿
    legal a.法律的；合法的
    legally adj合法地
    lemon n.柠檬,柠檬树
    lend vt.把...借给
    length n.长,长度；一段
    less a.更少的 ad.更少地
    lesson n.功课,课；课程
    let v.让
    letter n.信；证书；字母
    level n.水平面 a.水平的
    library n.图书馆(室)
    licence n. 自由,放肆
    license n.许可；执照 vt.准许
    lid n.(坛子、壶等)盖子
    lie vi.躺,平放；位于
    life n.生命,生活
    lift vt. 举起；抬起；升起,兴起；提起,提高；运送；吊；vi. (烟,云等)消散；起重机；升力；升起
    light n.光 adj.明亮的
    lightly ad.轻轻地,轻松地
    like prep.象；跟...一样
    likely a.可能的 ad.很可能
    limit n.限度；限制；范围
    limited a.有限的
    line vt.沿...排列 vi.排队
    link vt.有环连接 n.环
    lip n.嘴唇
    liquid n.液体 a.液体的
    list n.表；名单
    listen vi.听,留神听；听从
    literature n.文学；文献
    litre n. 升(容量单位)
    little adj.小的
    live vi.居住；活 a.活的
    lively adj.活泼的,有生气的
    living n.生活；谋生
    load vt.装,装载
    loan n.贷款；暂借 vt.借出
    local a.地方的；局部的
    locate vt.探明,找出,查出
    location n.定位,测位；测量
    lock n.锁 vt.锁上,锁住
    logic n.逻辑,推理；逻辑性
    logical a.逻辑的；符合逻辑的
    lonely adj.孤独的；荒凉的
    long vi.渴望；极想念
    look v.看
    loose a.松的；宽松的
    loosely ad. 松松地,松散地
    lord n.贵族；上帝,基督
    lorry n.运货汽车,卡车
    lose vt.失去；迷失；输掉
    loss n.遗失；损失；失败
    lost adj. 丢失的；迷途的；失败的；失去的；lose过去式；浪费掉的；失败了的；错过的；不知所措的；无望的,迷路的；丢途的
    loud a.响亮的；吵闹的
    loudly adv. 大声地；高声地；响亮地 a. 大声地,高声的
    love vt.爱,喜欢 n.爱
    lovely adj.可爱的；好看的
    lover n.爱好者；情人；情侣
    low adj.低的；浅的
    loyal a.忠诚的,忠心的
    luck n.运气
    lucky adj.幸运的,侥幸的
    luggage n.行李；皮箱,皮包
    lump vt.(使)成团 vi.结块
    lunch n.午餐,(美)便餐
    lung n.肺脏,肺
    machine n.机器；机械
    machinery n.(总称)机器；机构
    mad adj.发疯的；疯狂的
    magazine n.杂志,期刊
    magic n.魔法,巫术；戏法
    mail n.邮件；邮递
    main adj.主要的n.主要部分
    mainly adv.主要地；大部分
    maintain vt.维持；赡养；维修
    major a.较大的 n.专业
    majority n.多数；大多数
    make v.造,制作,使...
    make-up n. 捏造
    male a.男的,雄的 n.男子
    mall n.林荫小道
    man n.男人；人；人类
    manage vt.设法；对付
    management n.管理；经营,处理
    manager n.经理；管理人
    manner n.方式；态度；礼貌
    manufacture vt.制造 n.制造；产品
    manufacturer n.制造商；制造厂
    many a.许多的 pron.许多人
    map n.地图；图；天体图
    March n.三月
    mark n.痕迹；记号；商标
    market n. 市场；集市；行情；销路；市况,市场调查,市场研究；需要；需求；vt. (在市场上)销售；做买卖
    marketing n. 市场学,营销学；销售学；销售业务
    marriage n.结婚
    married adj. 已婚的,婚姻的；有配偶的
    marry vt.娶,嫁 vi.结婚
    mass n.(聚成一体的)团,块
    massive a.粗大的；大而重的
    master n.主人；能手；硕士
    match n.比赛,竞赛
    matching n. 匹配,调整；配合,协调,收支对应
    mate n.伙伴,同事；配偶
    material n.原料；材料
    mathematics n.数学
    matter n.事情
    maximum n.最大量 a.最大的
    may v.aux.可能,或许
    maybe adv.大概,或许
    mayor n.市长；镇长
    me pron. 我(i的宾格)
    meal n.(一)餐,(一顿)饭食
    mean vt.意思是...
    meaning n.意义,意思；意图
    means n.方法,手段,工具
    meanwhile ad.同时,当时
    measure vt.量,测量 n.分量
    measurement n.衡量,测量；尺寸
    meat n.肉
    media n. 媒体
    medical adj.医学的；医疗的
    medicine n.医学；内科学
    medium n.媒质；中间a.中等的
    meet n.会；集会
    meeting n.聚集,会合,会见
    melt vi.融化 vt.使融化
    member n.成员,会员
    membership n.成员资格；会员人数
    memory n.记忆；回忆；存储
    mental adj.精神的；脑力的
    mentally ad. 内心里
    mention vt.&n.提到,说起
    menu n.菜单；饭菜,菜肴
    mere a.仅仅的；纯粹的
    merely ad.仅仅,只不过
    mess n.混乱,混杂,肮脏
    message n.信息,消息；启示
    metal n.金属
    method n.方法,办法；教学法
    metre n.米,公尺
    midday n.正午,中午
    middle adj.中间的 n.中间
    midnight n.午夜(晚上十二点钟)
    might v.aux.可能,也许
    mild a.和缓的；温柔的
    mile n.英里
    military a.军事的；军人的
    milk vt.&vi.挤奶；出奶
    millimetre n.毫米
    mind vi.介意 vt.注意,当心
    mine pron.我的
    mineral n.矿物；矿石
    minimum n.最小量 a.最小的
    minister n.大臣；部长
    ministry n.(政府的)部
    minor a.较小的；较次要的
    minority n.少数；少数民族
    minute n.分钟
    mirror n.镜子 vt.反映,反射
    miss n.小姐
    missing a.缺掉的,失去的
    mistake n.错误 vi.误解,弄错
    mistaken adj.弄错的,错误的
    mix vt.&vi.混合；搅和
    mixed a. 混合的；混杂的,综合的；中等的,适度的,公道的
    mixture n.混合；混合物
    mobile a.运动的；流动的
    model n.模型；模式；模特儿
    modern adj.现代的
    moment n.片刻；瞬间；时刻
    Monday n.星期一
    money n.货币；金钱,财富
    monitor n.班长；监视器
    month n.月,月份
    mood n.心情,情绪；语气
    moon n.月球,月亮；卫星
    moral a.道德的；合乎道德的
    morally adv. 道德上；道义上
    more a.更多的 ad.更
    moreover ad.再者,加之,此外
    morning n.早晨,上午
    most a.最多的 ad.最,很
    mostly ad.主要的,大部分
    mother n.母亲
    motion n.运动；手势；提议
    motor n.发动机；机动车
    motorcycle n. 摩托车
    mount vt.登上,爬上 n.…山
    mountain n.山；山脉
    mouse n.鼠,耗子
    mouth n.嘴,口,口腔
    move n.行动,步骤
    movement n.动作,活动；移动
    movie n.电影；电影院
    moving a. 感人的,动的；活动的,移动,动人的,令人感动的n. & a. 活动的,自动的
    Mrs n. 夫人,太太；abb. 夫人,太太
    much ad.非常,很 a.许多的
    mud n.软泥,泥浆
    multiply vt.使增加；乘
    mum n.妈妈
    murder vt.&n.谋杀
    muscle n.肌肉
    museum n.博物馆
    music n.音乐
    musical adj.音乐的
    musician n.音乐家；作曲家
    must v.aux.必须；必然要
    my pron.我的
    myself pron.我自己
    mysterious adj.神秘的
    mystery n.神秘小说,侦探小说
    nail n.钉子 vt.将...钉牢
    naked a.裸体的；无遮敝的
    name n.名字；名誉 vt.说出
    narrow adj.狭窄的
    nation n.民族；国家
    national adj.国家的；民族的
    natural adj.自然的
    naturally adv. 自然地；天然地；必然地；天生地
    nature n.大自然,自然界
    navy n.海军
    near ad.近,接近 a.近的
    nearby adj.附近的 adv.附近
    nearly adv.几乎,差不多
    neat adj.整洁的；整齐的
    neatly ad. 整齐地
    necessarily adv.当然；必定,必然地
    necessary adj.必需的,必要的
    neck n.颈,脖子
    need vt.需要 v.aux.需要
    needle n.针,缝补,编织针
    negative a.负的,阴性的
    neighbour n.邻居；邻人
    neighbourhood n.邻居关系；邻近
    neither adj.&pron.(两者)都不
    nephew n.侄子,外甥
    nerve n.神经；勇敢,胆量
    nervous adj.神经质的
    nervously adv. 紧张不安地；神情激动地；神经质地；胆怯地
    nest vi.筑巢 vt.为…筑巢
    net vt.用网捕；用网覆盖
    network n.网状物；网络
    never adv.从来没有；决不
    nevertheless conj.然而 ad.仍然
    new adj.新的
    newly ad.新近,最近
    news n.新闻,消息
    newspaper n.报纸
    next a.紧接的；贴近的
    nice adj.好的,好看的
    nicely ad. 恰好地；谨慎地
    niece n.侄女,甥女
    night n.夜,夜间
    no adv.不,不是
    nobody pron.没有人
    noise n.喧闹声；响声；噪声
    noisily adv. 喧闹地
    noisy a.嘈杂的；喧闹的
    none pron.没有人 ad.毫不
    nonsense n.胡说,废话
    nor conj.也不；不
    normal adj.正常的,正规的
    normally adv. 通常地；一般地；正常地；平常地
    north n.北部,北方
    northern a.北方的,北部的
    nose n.鼻子
    not ad.不,没有
    note n.钞票,纸币；笔记
    nothing n.没有东西 ad.毫不
    notice vt.注意 n.通知；注意
    noticeable a.显而易见的；重要的
    novel n.小说 a.新的
    November n.十一月
    now ad.现在；立刻；于是
    nowhere ad.任何地方都不
    nuclear a.原子核的；核心的
    number vt.共计,达…之数
    nurse n.护士
    nut n.坚果,干果；螺母
    obey vt.顺从 vi.服从
    object n.物,物体；目的
    objective a.客观的；无偏见的
    observation n.注意；观察；观察力
    observe vt.&vi.观察
    obtain vt.获得,得到,买到
    obvious adj. 明显的,显著的；显而易见的；清楚的；明白的
    obviously adv.显而易见地
    occasion n.场合,时刻；时机
    occasionally adv.偶然；非经常地；偶而,有时
    occupy vt.占领；占,占有
    occur vi.发生；出现,存在
    ocean n.海洋；洋
    October n.十月
    odd a.奇数的；单只的
    oddly ad. 奇妙地,奇怪地,单数地
    of prep....的
    off prep.&adv.(离)开
    offence n.犯罪,犯规；冒犯
    offend vt.冒犯 vi.犯过错
    offensive a.冒犯的；进攻的
    offer vt.提供；提出 n.提供
    office n.办公室；处,局,社
    officer n.军官
    official adj.官方的,正式的
    officially ad. 作为公务员,职务上,官方地
    often ad.经常,常常
    oh int.嗬,哦,唉呀
    oil n.油；石油 vt.加油于
    OK adv.对；好；可以
    old a.老的；…岁的
    old-fashioned a. 旧式的,保守的,挑剔的
    on prep.在...上
    once ad.一次；曾经 n.一次
    one pron.一(个,只...)
    onion n.洋葱,洋葱头
    only ad.只,仅仅 a.唯一的
    onto prep.到…上
    open a.开的；开放的 vt.开
    opening a.开始的 n.开始
    openly ad. 公开地；直率地
    operate vi.&vt.动手术；操作
    operation n.运算
    opinion n.意见,看法,主张
    opponent n.对手,敌手；对抗者
    opportunity n.机会,良机
    oppose vt.反对；反抗
    opposed a. 反对的
    opposite adj.对面的；相对的
    opposition n. 反对；敌对
    option n.选择,取舍
    or conj.或者
    orange n.橙子,桔子
    order n.定货；定货单
    ordinary a.平常的；平凡的
    organ n.器官；机构；管风琴
    organization n.组织；团体,机构
    organize vt.组织,编组
    origin n.起源；开端
    original a.最初的；新颖的
    originally adv. 原来,当初；最初；本来；独创地
    other pron.另一个人(或物)
    otherwise ad.另外；在其他方面
    ought v.aux 早应该,本应
    our pron.我们的
    ours pron.我们的
    ourselves pron.我们自己
    out ad.出,在外；现出来
    outdoor a.户外的,室外的
    outdoors ad.在户外,在野外
    outer adj.外部的
    outline n.轮廓；略图；大纲
    output n.产量；输出量；输出
    outside n.外部；外表a.外部的
    outstanding a.突出的,杰出的
    oven n.炉,灶；烘箱
    over adv.结束,完了
    overall n.工装裤 a.全面的
    overcome vt.战胜,克服
    owe vi. & vt. 欠(债等)；感激；欠应该支付…；应该把…归功于
    own vt.所有；拥有
    owner n.物主,所有人
    pace n.(一)步(距离)；步速
    pack vt.捆扎；挤满 n.包
    package n.包裹；包装
    packaging n. 包装；打包
    packet n.小包(裹),小捆
    page n.页,页码
    pain n.疼；疼痛
    painful a.使痛的；费力的
    paint vt.漆,画 n.油漆
    painter n.漆工,画家,绘画者
    painting n.油画；绘画；着色
    pair n.一对 vi.成对,配对
    palace n.宫,宫殿
    pale a.苍白的；浅的
    pan n.平底锅,盘子
    panel n.专门小组；面,板
    pants n.裤子；男用短衬裤
    paper vt.用纸包装(或覆盖)
    parallel a.平行的；相同的
    parent n.父(母)亲
    park n.公园
    parliament n.议会,国会
    part n.一部分；零件；本份
    particular a.特殊的；特定的
    particularly ad.特别,尤其,格外
    partly ad.部分地,不完全地
    partner n.伙伴；搭挡；配偶
    partnership n. 合伙,合股
    party n.聚会
    pass v.传递(用具等)
    passage n.通过；通路,通道
    passenger n.乘客；旅客
    passport n.达到目的的手段
    past prep.过；经过
    path n.路,小道；道路
    patience n.忍耐,容忍,耐心
    patient a.忍耐的 n.病人
    pattern n.型,式样,模,模型
    pause vi.&n.中止；暂停
    pay vt.给...报酬 n.工资
    payment n.支付,支付的款项
    peace n.和平
    peaceful a.和平的；安静的
    peak n.山顶,巅 a.最高的
    pen n.钢笔
    pence n. 便士(英货币)；penny的复数
    pencil n.铅笔
    penny n.便士(英国辅币单位)
    pension n.抚恤金,年金
    people n.人民,民族；人
    pepper n.胡椒,胡椒粉
    per prep.每,一
    perfect adj.极好的,完美的
    perfectly adv. 极好地,完美地；十分地；很,完全
    perform vt.履行;表演 vi.行动
    performance n.履行；演出；行为
    performer n. 表演者
    perhaps adv.也许,可能
    period n.时期；学时；句号
    permanent a.永久的,持久的
    permanently adv. 永久地；持久地
    permission n.允许,许可,同意
    permit vt.允许 n.执照
    person n.人；人身；本人
    personal a.个人的；本人的
    personality n.人格,个性；人物
    personally adv. 亲自,就个人而言
    persuade vt.劝说；说服
    pet n.爱畜；宠儿a.宠爱的
    petrol vt. 加以汽油；n. (英)汽油；石油
    phase n.阶段；方面；相位
    philosophy n.哲学；哲理；人生观
    phone n. & vt. & vi. 电话机；打电话
    photocopy n. & v. 影印,照像复印
    photograph n.照片,相片
    photographer n. (报纸、杂志等之) 摄影者,摄影家
    photography n.摄影术
    phrase n.短语；习惯用语
    physical adj.物理的
    physically adv. 物质上,身体上；按照自然规律；a. 物理上,实际上
    physics n.物理学
    piano n.钢琴
    pick n.镐,鹤嘴锄
    picture n.图画,照片
    piece n.(文艺作品的)篇,首
    pig n.猪
    pile vt.堆积,堆起
    pill n.药丸,丸剂
    pilot n.领航员；飞行员
    pin n.针,饰针 n.别住
    pink n.粉红色 a.粉红色的
    pint n.品脱
    pipe n.管子,导管,输送管
    pitch n.沥青
    pity n.怜悯；遗憾 vt.同情
    place n.地方,地点；住所
    plain n.平原 a.清楚的
    plan n.&vt.计划,打算
    plane n.平面；飞机
    planet n.行星
    plant n.植物；工厂 vt.栽种
    plastic a.塑料的；塑性的
    plate n.盘子；碟子
    platform n.政纲,党纲,宣言
    play n.戏剧,表演；玩耍
    player n.比赛者,选手
    pleasant adj.令人愉快的
    pleasantly ad. 愉快地；令人愉快地；舒适地
    please vt.使高兴,请vi.满意
    pleased adj. 高兴的；欣喜的；乐意的
    pleasing a. 令人喜爱的,愉快的,舒适的
    pleasure n.愉快,快乐；乐事
    plenty n.充足；大量
    plot n.小块土地 vt.密谋
    plug vt.接上插头通电
    plus prep.加
    pocket n.衣袋
    poem n.诗,韵文；诗体文
    poetry n.诗,诗歌,诗作
    point n.观点；论点；要点
    pointed adj. 一针见血的；尖(锐)的；中肯的
    poison vt.使中毒
    poisonous adj.有毒的；有害的
    pole n.杆；柱
    police n.警察；警察当局
    policy n.政策,方针
    polish vt.磨光；使优美
    polite a.有礼貌的；有教养的
    politely adv. 有礼貌地；温和地；文雅地；客气地
    political adj.政治的
    politically ad.政治上
    politician n.政治家；政客
    politics n.政纲,政见,策略
    pollution n.污染
    pool n.小池；水塘
    poor adj.可怜的；贫穷的
    pop n.流行音乐,流行歌曲
    popular adj.大众的；流行的
    population n.人口；全体居民
    port n.港,港口
    pose vt.(使)摆好姿势
    position n.主张,立场；形势
    positive a.正的；阳性的
    possess vt.占用,拥有(财产)
    possession n.所有；拥有；财产
    possibility n.可能；可能的事
    possible adj.可能的
    possibly adv.可能地；也许
    post vt.投寄,邮寄 n.邮局
    pot n.罐；锅；壶
    potato n.土豆
    potential a.潜在的 n.潜力
    potentially ad. 潜在地；可能地,大概地
    pound n.英镑(英国货币单位)
    pour vt.灌,倒 vi.倾泻
    powder n.粉末；药粉；火药
    power n.能力；力；权；幂
    powerful a.强有力的；有权威的
    practical adj.实际的；应用的
    practically ad.实际上；几乎
    practice n.实践；练习；业务
    practise vt.练习
    praise vt.&n.赞扬,表扬
    prayer n.祈祷,祈求
    precise a.精确的,准确的
    precisely adv.正好；正确地；严密的；精确地；刻板地；明确地
    predict v.预言,预告,预测
    prefer vt.宁可,宁愿
    preference n.偏爱,优先；优先权
    pregnant a.怀孕的；意义深长的
    premises n. 建筑物；房屋,房产
    preparation n. 准备,预备；制备；预习(时间)；配制；安排,筹备,制剂
    prepare vt.&vi.准备；预备
    prepared adj. 准备好的,预制的
    presence n.出席,到场；在
    present a.现在的 n.目前
    presentation n.介绍；赠送；呈现
    preserve vt.保护；保存；腌渍
    president n.总统
    press n.印刷机,印刷所
    pressure n.压力；压力；压,按
    presumably adv. 也许,大概；推测起来；假定地,推测地
    pretend vt.假托,借口vi.假装
    pretty a.漂亮的,标致的
    prevent vt.预防,防止；阻止
    previous a.先的；前的 ad.在前
    previously adv. 预先,先前；以前
    price n.价格；代价
    pride n.骄傲；自满；自豪
    priest n.教士,牧师,神父
    primarily ad.首先；主要地
    primary a.最初的；基本的
    prime adj.首要的；基本的
    prince n.王子,亲王
    princess n.公主,王妃
    principle n.原则,原理；主义
    print vt.&n.印刷
    printer n.印刷工；印花工
    printing n. 印刷；印刷术；印刷业；a. 印刷
    prior a.在先的；优先的
    priority n.先,前；优先,重点
    prison n.监狱,监禁
    prisoner n.囚犯
    private a.私人的；私下的
    privately adv. 私下地,秘密地；一个人
    prize n.奖赏,奖金 vt.珍视
    probable a.或有的；大概的
    probably adv.很可能,大概
    problem n.问题；习题,问题
    procedure n.程序；手续；过程
    proceed vi.进行；继续进行
    process n.过程；制作法；工序
    produce vt.生产；产生；展现
    producer n.生产者；舞台监督
    product n.产品,产物；(乘)积
    production n.生产；产品；总产量
    profession n.职业
    professional a.职业的 n.专业人员
    professor n. 教授；索比教授；宣称者；声明者
    profit n.益处；利润 vi.得益
    program vi.编制程序
    programme n.程序
    progress n.前进,进展；进步
    project n.方案,工程 vi.伸出
    promise n.诺言 vt.&vi.答应
    promote vt.促进,发扬；提升
    promotion n.促进；提升；创立
    prompt a.及时的 vt.敦促
    promptly adv. 立刻地；迅速地,准时地；敏捷地,及时地,即时地；果断地adj. 迅速地
    pronounce vt.发…的音；宣布
    pronunciation n.发音,发音法
    proof n.证据；证明；论证
    proper a.合乎体统的,正派的
    properly adv. 妥善地；恰当地；适当地；彻底地；合适地；严格地；真正地
    property n.财产；财产权
    proportion n.比,比率,部分
    proposal n.提议,建议；求婚
    propose vt.提议 vi.求婚
    prospect n.展望；前景,前程
    protect vt.保护
    protection n.保护,警戒
    protest vt.&vi.&n.抗议
    proud adj.骄傲的；自豪的
    proudly adv. 骄傲地；自豪地；傲慢地
    prove vt.证明,证实
    provide vt.提供；装备,供给
    provided conj.以…为条件
    pub n. 酒店
    public adj.公共的,公众的
    publication n.公布；出版；出版物
    publicity n. 公开,名声,宣传
    publicly adv. 公开地；公然；公众所有地
    publish vt.&vi.出版；发行
    pull vt.拉,拖；拉,拉力
    punch vt.冲出 n.冲压机
    punish vt.&vi.惩罚；处罚
    punishment n.罚,惩罚,处罚
    pupil n.小学生；学生
    purchase n.买,购买 vt.买
    pure a.纯粹的；纯洁的
    purely adv. 全然,纯然；纯粹地,完全地；仅仅；简单地
    purple n.紫色 a.紫的
    purpose n.目的；意图；效果
    pursue vt.追赶,追踪；进行
    push vt.推,逼迫 vi.推
    put vt.放,摆；使处于
    qualification n.资格；限制条件
    qualified adj. 有资格的；合格的；受限制的；有限度的,胜任的
    qualify vt. 修饰,限定；使合格；使胜任；使具有资格；限制；vi. 取得资格
    quality n.品质
    quantity n.数量
    quarter n.四分之一；一刻钟
    queen n.女王；王后
    question n.发问；问题；疑问
    quick adj.快的,迅速的
    quickly adv.迅速地；快速地；快地；敏捷地
    quiet adj.安静的,平静的
    quietly adv. 安静地,平静地；轻轻地；静悄悄地,平稳地；静静地；静止地；寂静地
    quit vt.离开,退出；停止
    quite adv.很,十分
    quote vt.引用,引证；报价
    race n.比赛；赛跑；赛马
    racing n. 竞赛,赛跑,竞走
    radio n.收音机
    rail n.铁轨；轨道；铁路
    railway n.铁路,铁道
    rain v.下雨 n.雨
    raise vt.提出,发起,发出
    range vt.排列；把…分类
    rank n.排,横行；社会阶层
    rapid adj.快的,迅速的
    rapidly adv. 迅速地,急速地；敏捷地；险峻地
    rare a.稀薄的；稀有的
    rarely ad.很少,难得
    rate n.比率；速率；等级
    rather ad.宁可,宁愿；相当
    raw a.未煮过的；未加工的
    reach vt.&vi.伸手去够..
    react vi.起反应；有影响
    reaction n.反应；反作用
    read v.读
    reader n.读者；读物,读本
    reading n.读,阅读；读书
    ready adj.准备好的,有准备
    real a.真的；现实的
    realistic a.现实的；现实主义的
    reality n.现实；真实
    realize vt.意识到
    really ad.真正地；实在
    rear n.后部,后面；背面
    reason n.理由；理性 vi.推理
    reasonable adj.有道理的
    reasonably adv. 合理地,适当地；相当地；有理地；adj. 合情合理地
    recall n. 回想；vt. 回忆,回想起；想到,叫回；收回；召回,忆起,记忆；撤消,取消；复活,检索
    receipt n.收到；收条,收据
    receive vt.收到,接到
    recent a.新近的,最近的
    recently adv.近来
    reception a.接待；招待会；接受
    reckon vi.数,算帐 vt.认为
    recognition n.认出,识别；重视
    recognize vt.认识,认出；承认
    recommend vt.推荐,介绍；劝告
    record n.记录,记载；唱片
    recording n. 录音,记录
    recover vt.重新获得；挽回
    red adj.红色的
    reduce vt.缩减；减少
    reduction n.减少,减小,缩减
    refer vt.把...提交 vi.提出
    reference n.参考文献；参照系
    reflect vt.反射；反映；思考
    reform vt.&n.改革,改良
    refrigerator n.冰箱,冷藏库
    refusal n.拒绝
    refuse vt.拒绝 vt.拒绝
    regard vt.把…看作；尊敬
    regarding prep.关于
    region n.地区,地带；领域
    regional adj. 地区的,区域的；地方的,局部的
    register n.&vt.登记,注册
    regret vt.&vi.遗憾,抱歉
    regular a.规则的；整齐的
    regularly adv. 规则地；经常地；定期地；有规律地；整齐地
    regulation n.规章,规则；调节
    reject vt.抛弃；拒收
    relate vt.叙述；使联系
    related adj. 有亲缘关系的；与…有关的；叙述的；有联系的；相关的
    relation n.关系,联系；家属
    relationship n.关系,联系
    relative a.有关系的；相对的
    relatively adv. 比较地,相对地
    relax vt.&vi.(使)松驰,放松
    relaxed adj. 轻松的；松懈的,不拘束的
    release vt.释放；放松；发表
    relevant a.有关的,贴切的
    relief n.宽慰；欣慰
    religion n.宗教；宗教信仰
    religious adj.宗教的；虔诚的
    rely vi.依赖,依靠；信赖
    remain vi.保持,仍是；剩下
    remaining a.剩余的
    remains n.剩下的东西,残余
    remark vt.&vi.&n.评论,谈论
    remarkable a.异常的,非凡的
    remarkably ad. 非凡地；显著地
    remember vt.记得,想起；记住
    remind vt.使想起
    remote a.相隔很远的；冷淡的
    removal n.移动；迁移；除掉
    remove vt.移动,搬开；脱掉
    rent n.租金,租 vi.出租
    repair vt.&n.修理,修补
    repeat vt.重说,重做 n.重复
    repeated a. 反复的；重复的
    repeatedly ad.重复地；一再
    replace vt.把…放回；取代
    reply vt.&n.回答；答复
    report vt.,vi.&.n.报告,汇报
    represent vt.描绘；代表；象征
    representative a.代表性的 n.代表
    reproduce vt.&vi.繁殖,生殖
    reputation n.名誉,名声；好名声
    request n.&vt.请求；要求
    require vt.需要；要求
    requirement n.需要；要求
    rescue vt.&n.营救；援救
    research n.调查；研究
    reservation n.保留；预定,预订
    reserve vt.储备,保留；预定
    resident a.居住的 n.居民
    resist vt.&vi.抵抗；抵制
    resistance n.抵抗；抵制；抵抗力
    resolve vt.解决；决心 n.决心
    resort vi.&n.求助,凭借
    resource n.资源
    respect n.&vt.尊敬,尊重
    respond vi.作答；响应
    response n.作答,回答；响应
    responsibility n.责任,责任心；职责
    responsible a.重要的；可靠的
    rest vi.&vt.(使)支撑(在)
    restaurant n.餐馆,饭店,菜馆
    restore vt.恢复；归还；修补
    restrict vt.限制,限定,约束
    restricted a. 受限制的,受约束的
    restriction n.限制,限定,约束
    result n.结果；效果
    retain vt.保持,保留,保有
    retire vi.退下；引退；就寝
    retired adj. 退休的；通职的
    retirement n.退休,引退；退隐
    return vi.&n.回来,返回
    reveal vt.展现；揭示,揭露
    reverse vt.颠倒,翻转 n.背面
    review vt.再检查 n.复习
    revise vt.修订,校订；修改
    revision n. 校订,修正,修订本
    revolution n.革命；旋转,绕转
    reward n.报答；报酬 vt.奖赏
    rhythm n.韵律,格律；节奏
    rice n.米饭；大米
    rich adj.有钱的,富裕的
    rid vt.使摆脱,使去掉
    ride vt.&vi.骑(马,自行车)
    rider n.骑马的人；乘车的人
    ridiculous a.荒谬的,可笑的
    right adv.正好,恰恰
    rightly ad. 应该；正义地；正确地
    ring n.环形物(如圈、环等)
    rise vi.起立；升起；上涨
    risk n.风险,危险,冒险
    rival n.竞争者 a.竞争的
    river n.江,河
    road n.路,道路,公路
    rob vt.掠夺；抢劫
    rock vt.摇,使动摇 vi.摇
    role n.角色,作用,任务
    roll vi.打滚；滚动
    romantic a.浪漫的；传奇的
    roof n.屋顶；顶,顶部
    room n.房间
    root n.根,根子 vi.生根
    rope n.绳子
    rough a.表面不平的；粗略的
    roughly adv. 粗暴地；粗糙的；粗野地；粗鲁地；大致地；大约地,粗略地；毛糙地；大体上
    round prep.围(绕)着
    route n.路；路线
    routine n.例行公事 a.日常的
    row n.(一)排,(一)行
    royal a.王的；皇家的
    rub vt.&vi.摩擦
    rubber n.橡皮
    rubbish n.垃圾,废物；废话
    rude adj.无礼的；粗鲁的
    rudely ad. 粗鲁地,原始地；粗略地
    ruin n.毁灭；废墟 vt.毁坏
    ruined a.破坏的；毁坏
    rule n.规则；规定
    ruler n.尺
    rumour n.谣言,谣传,传闻
    run v.跑
    runner n.赛跑的人
    running n. 跑步；经营；adj. 连续的；奔跑的；流动的；运行着的,游动的
    rural a.农村的,田园的
    rush vi.冲,奔 vt.催促
    sack n.袋,麻袋；开除
    sad adj.悲哀的
    sadly adv. 难过地,悲哀地；痛心的；伤心的；悲痛地,可惜；凄惨地；忧愁地悲哀地
    sadness n.悲痛,悲哀
    safe adj.安全的
    safely adv. 安全地；平安地；可靠地；平安地；确实地
    safety n.安全,保险
    sail vi.航行
    sailing adj. 启航的；n. 航行；驶行,航海,开航
    sailor n.水手,海员,水兵
    salad n.色拉；莴苣,生菜
    salary n.薪金,薪水
    sale n.卖,销售
    salt n.盐
    salty adj. 咸的；盐的
    same adj.同样的
    sample n.样品；实例,标本
    sand n.沙,沙地
    satisfaction n.满意；快事；赔偿
    satisfy vt.使满意；使满足
    satisfying a. 令人满意的
    Saturday n.星期六
    sauce n.调味汁,酱汁
    save vt.救,挽救
    saving n. 搭救；节约；存款；储蓄a. 保存的；补偿的；储蓄,存款,节约的；挽救的
    say v.说,讲
    scale n.天平,磅秤,秤
    scare vt.惊吓 vi.受惊
    scared adj. 怕；惊慌的,吓坏了的；害怕的,恐惧的
    scene n.(戏剧等的)一场
    schedule n.时间表；计划表
    scheme vt.计划 vi.搞阴谋
    school n.学校
    science n.科学
    scientific adj. 科学的；科学(上)的
    scientist n.(自然)科学家
    scissors n.剪刀,剪子
    score n.二十；(比赛)得分
    scratch vt.&vi.&n.搔；抓
    scream vi.尖叫；呼啸
    screen n.屏；屏幕 vt.掩蔽
    screw n.螺旋,螺丝 vt.拧紧
    sea n.海洋,海
    seal n.封蜡；印记 vt.封
    search vt.在…中搜寻,搜查
    season n.季,季节,时节
    seat n. 座；座部；座位；中心；席位；所在地,场所；v. 就座；容纳
    second num.第二 a.二等的
    secondary a.第二的；次要的
    secret n.秘密
    secretary n.秘书；书记；大臣
    secretly ad. 秘密地；隐蔽地
    section n.切下的部分
    sector n. 扇形,尺规,函数尺
    secure a.安心的；安全的
    security n.安全,安全感
    see v.看,看见；了解
    seed n.种子
    seek vt.寻找,探索；试图
    seem vi.好像,似乎
    select vt.&vi.选择；挑选
    selection n.选择,挑选；精选物
    self n.自我,自己
    sell vt.&vi.卖
    senate n.参议院,上院
    senator n.参议员；评议员
    send vt.送；派遣；发射
    senior a.年少的；地位较高的
    sense n.感官；感觉；见识
    sensible adj. 合情合理的；感觉得到的；明智的；感知的；明显的；通情达理的；可察觉的；明理的
    sensitive a.敏感的；灵敏的
    sentence vt.判决,宣判
    separate a.分离的；个别的
    separated a. 分开的
    separately adj. 分离地；单独地；adv. 分别地；分离地；孤独地；各别地,单独地
    separation n.分离,分开；分居
    September n.九月
    series n.连续,系列；丛书
    serious a.严肃的；认真的
    seriously adv. 严肃地,严重地；认真地；重大
    servant n.仆人,佣人
    serve vt.开(饭),上(菜)
    service n.服务
    session n.会议,一段时间
    set n.(一)套 vt.镶,嵌
    settle vt.安排；安放；调停
    several adj.&pron.几个,数个
    severe a.严格的；严厉的
    severely adv. 严厉地,苛刻地；严肃地；严格地；剧烈地
    sew vi缝纫 vt.缝制,缝补
    sewing n. 缝纫,缝制物；(书的)装订
    sex n.性别,性
    sexual a. 性的,性别的
    shade n.(色彩的)浓淡,深浅
    shadow n.影子
    shake vt.摇,使震动 n.摇动
    shall v.aux.(我,我们)将要
    shallow a.浅的；浅薄的
    shame n.羞耻,羞愧；羞辱
    shape n.形状；情况 vt.形成
    share vt.分享 n.一份
    sharp adj.锋利的；尖的
    sharply ad.锐利地,敏锐地
    shave vt.剃,刮 vi.修面
    she pron.她
    sheep n.羊,绵羊
    sheet n.被单；纸张；薄板
    shelf n.搁板,架子
    shell n.炮弹,猎枪子弹
    shelter n.隐蔽处；掩蔽,庇护
    shift vt.替换,转移 n.转换
    shine v.照耀；发光
    shiny a. 有光泽的,发光的,辉煌的
    ship n.轮船
    shirt n.(男试)衬衫
    shock n.冲击；震惊 vi.震动
    shocking a. 令人震惊的；可怕的
    shoe n.鞋
    shoot vt.发射；射中 n.发芽
    shooting n. 射击
    shop n.商店,店铺；车间
    shopping n. 买东西；购物
    short adj.矮的
    shortly adv.立刻；不久
    shot n.发射；射击声
    should aux.v.将；万一；就
    shoulder vt.承担,挑起,肩负
    shout vi.vt.&n.喊；高呼
    show vt.给…看；表明
    shower vi.下阵雨 vt.使湿透
    shut vt.&vi.关闭
    shy a.易受惊的；害羞的
    sick a.有病的；恶心的
    side n.边；面
    sideways ad.斜向一边地
    sight n.视力；视觉；见
    sign n.征兆,迹象,病症
    signal n.信号 vi.发信号
    signature n.署名,签字,签名
    significant n.有意义的；重要的
    silence n.寂静,沉默
    silent a.沉默的；寂静无声的
    silk n.(蚕)丝；丝织品,绸
    silly a.傻的,愚蠢的
    silver n.银；银子；银器
    similar a.相似的,类似的
    similarly adv. 同样地；类似地,相似地
    simple adj.单纯的；简易的
    simply adv.简单地；仅仅
    since conj.由于；既然
    sincere a.真诚的；真挚的
    sincerely adv. 真诚地；诚恳地；真挚地
    sing v.唱,演唱
    singer n.歌唱家,歌手
    singing n. 唱歌
    single a.单一的；独身的
    sink n.(厨房内的)洗涤槽
    sir n.先生,阁下；…爵士
    sister n.姐、妹
    sit v.坐
    site n.地点,地基；场所
    situation n.位置；处境；形势
    size n.尺寸,大小
    skilful a. 精巧的；熟练的；灵巧的
    skill n.技能,技巧；熟练
    skilled a.有技能的,熟练的
    skin n.皮,皮肤
    skirt n.女裙
    sky n.天空
    sleep v.&n.睡,睡眠
    sleeve n.袖子,袖套
    slice n.薄片,切片；部分
    slide vi.滑动
    slight a.细长的；轻微的
    slightly adv. 轻微地；轻蔑地；略微地；稍微,有点；细长的；轻轻地
    slip vt.&vi.(使)滑动
    slope n.倾斜；斜面 vi.倾斜
    slow a.慢的；迟钝的
    slowly adv. 慢慢地；缓慢地；减速地,adj. 慢慢地
    small a.小的,少的；小型的
    smart a.巧妙的；洒脱的
    smash vt.粉碎；击溃；猛掷
    smell n.嗅觉；气味 vt.嗅
    smile v.微笑
    smoke n.烟；抽烟 vi.冒烟
    smoking n. 吸烟；冒烟；熏制；抽烟
    smooth adj.光滑的；平静的
    smoothly adv. 顺利地,通顺地；光滑地；平稳地；安稳地；流畅地；平滑地,流利地
    snake n.蛇
    snow n.雪 vi.下雪
    so adv.这么,那么
    soap n.肥皂
    social a.社会的；社交的
    socially ad. 社交上；社会上
    society n.社会；会；社团
    sock n.短袜
    soft adj.软的；柔和的
    softly adv. 柔软地；轻轻地；温柔地；温和地；软化地；柔和地
    software n.(计算机的)软件
    soil n.土壤；土地
    soldier n.士兵,战士
    solid a.固体的 n.固体
    solution n.解决,解答；溶解
    solve vt.解答；解决
    some adj.&pron.一些
    somebody pron.某人,有人
    somehow ad.由于某种原因
    something pron.某事,某物
    sometimes ad.不时,有时
    somewhat pron.一点儿 ad.有点
    somewhere ad.在某处 n.某地
    son n.儿子
    song n.歌曲
    soon adv.不久；很快
    sore a.痛的；恼火的 n.疮
    sorry a.难过的；对不起的
    sort n.种类；类别 vt.整理
    soul n.灵魂；精神；人
    sound a.健康的；完好的
    soup n.汤
    sour a.酸的；脾气坏的
    source n.来源；根源
    south n.南,南方 a.南方的
    southern adj.南方的,南部的
    space n.空间；场地；空白
    spare vt.节约 a.多余的
    speak v.说话
    speaker n.场声器
    special adj.特别的；特殊的
    specialist n.专家
    specially ad.专门地,特别地
    specific a.特有的；具体的
    specifically ad. 特定的,明确的
    speech n.言语,讲话
    speed n.速度
    spell vt.拼写 vi.拼字
    spelling n.拼字,拼法,拼写法
    spend vt.用钱,花费；度过
    spice n.香料,调味品；香气
    spicy a. 香的,多香料的,辛辣的,下流的
    spider n.蜘蛛
    spin vt.纺；使旋转 n.旋转
    spirit n.精神；气魄；情绪
    spiritual a.精神的,心灵的
    spite n.恶意,怨恨
    split n.分裂,分化；派系
    spoil vt.损坏,糟蹋；宠坏
    spoken speak的过去分词；a. 口头的；口语的；说
    spoon n.匙,调羹
    sport n.运动
    spot n.点；班点；地点
    spray vt.&vi.向...喷射；喷
    spread vt.伸开；传播 n.传播
    spring n.春天,春季
    square n.正方形；广场
    squeeze vt.&vi.榨,挤；压榨
    stable a.稳定的,不变的
    staff n.工作人员；参谋
    stage n.舞台；戏剧；阶段
    stair n.(常用复数)楼梯
    stamp n.戳子；邮票；标志
    stand vi.站；坐落 n.架,台
    standard n.标准 a.标准的
    star vt.&vi.主演
    stare vi.&vt.盯,凝视
    start vt.开始 vi.出发
    state n.州；国家；政府
    statement n.陈述,声明
    station vt.驻扎；安置
    statue n.塑像,雕像,铸像
    status n.地位,身分
    stay vi.停留；暂住
    steadily ad.稳定地,不变地
    steady a.坚定的,扎实的
    steal vt.偷,窃取
    steam n.蒸汽 vi.蒸发 vt.蒸
    steel n.钢
    steep a.险峻的,陡峭的
    steeply ad. 陡峭地
    steer vt.&vi.驾驶
    step n.(脚)步；步骤 vi.走
    stick vt.&vi.伸,伸出
    sticky a.粘性的；胶粘的
    stiff a.硬的；僵直的
    stiffly ad. 硬；顽固地
    still adj.寂静的；静止的
    sting vt.刺；刺痛 vi.&n.刺
    stir vt.动；拨动；激动
    stock n.原料；库存品；股本
    stomach n.胃；肚子；食欲
    stone n.果核,(水果的)硬核
    stop vt.塞住；阻止；停止
    store vt.存贮,储藏
    storm n.风暴；暴(风)雨
    story n.故事,小说,传说
    stove n.炉,火炉,电炉
    straight a.直的；正直的 ad.直
    strain vt.拉紧 vi.尽力
    strange a.陌生的；奇怪的
    strangely adv. 奇怪的；陌生地
    stranger n.陌生人；新来者
    strategy n.战略；策略
    stream n.(小)河；溪流
    street n.街道
    strength n.力量；力气
    stress n.压力；重音 vt.着重
    stretch vt.伸展 vi.伸 n.伸展
    strict a.严格的；严谨的
    strictly adv. 全然；严格地,严谨地；绝对；明确地；adj. 严厉地,严格地
    strike vt.&vi.打；击
    striking a.显著的,惊人的
    string n.细绳；带子
    strip n. 条带；细长条,条；窄条,长带；带状物；一片,一条；狭长的一片；vt. 剥(光)；夺；剥去；剥夺,脱去…的衣服vi. 剥,剥去；脱光衣服；
    stripe n.条纹,条子
    striped adj. 有条纹的
    stroke n.打,击；鸣声；中风
    strong adj.坚固的；强有力的
    strongly adv. 强有力地；强壮地,强烈地
    structure n.结构；构造 vt.建造
    struggle n.&vi.斗争,奋斗
    student n.学生
    studio n.工作室；播音室
    study v.学习
    stuff n.材料 vt.装,填,塞
    stupid a.愚蠢的；感觉迟钝的
    style n.风格；文体；式样
    subject n.题目；学科；主语
    substance n.物质；实质；本旨
    substantial a.物质的；坚固的
    substantially ad. 大体上；本质上；实质上
    substitute n.代替人 vt.用…代替
    succeed vt.继…之后 vi.成功
    success n.成功,成就,胜利
    successful a.成功的,结果良好的
    successfully adv. 成功地；有成绩地；出色地；结果良好地
    such adv.那么 adj.这样的
    suck vt.吮吸；舐食
    sudden a.突然的,意外的
    suddenly adv. 突然地；忽然；a.突然的
    suffer vi.受苦 vt.遭受
    suffering n.痛苦；苦难
    sufficient a.足够的,充分的
    sufficiently adv. 充分地,足够地
    sugar n.糖
    suggest vt.建议；暗示
    suggestion n.建议,意见；暗示
    suit n.一套(衣服)
    suitable a.合适的；适宜的
    suitcase n.小提箱,衣箱
    sum n.总数；金额 vi.共计
    summary a.概括的；速决的
    summer n.夏,夏季
    sun n.太阳,日
    Sunday n.星期日,礼拜日
    superior a.较高的；优越的
    supermarket n.超级市场
    supply vt.&n.供给,供应
    support vt.支撑；支持；维持
    supporter n. 支持者,后盾,伴随者
    suppose vt.假定；猜想
    sure adj.确信的,肯定的
    surely adv. 确实,一定；当然；必定地,无疑地；肯定,谅必；a. 确实；稳当地
    surface n.地面,表面；外表
    surname n.姓
    surprise n.惊奇,诧异
    surprised a. 惊讶的
    surprising a.惊人的；出人意外的
    surprisingly ad. 惊人地；意外地
    surround vt.围,围绕,圈住
    surrounding n. 周围的事物；环境；adj. 环绕的；周围的；包围
    surroundings n.周围的事物,环境
    survey vt.俯瞰；检查；测量
    survive vt.幸免于 vi.活下来
    suspect vt.怀疑 vi.疑心
    suspicion n.怀疑,疑心,猜疑
    suspicious a.可疑的；猜疑的
    swallow n.,vt.&vi.吞,咽
    swear vt.宣(誓) vi.诅咒
    sweat n.汗
    sweater n.厚运动衫,毛线衫
    sweep vi.掠过；袭来
    sweet adj.甜的
    swell vi.&vt.使膨胀,隆起
    swim vi.游,游泳；眼花
    swimming n. 游水,目眩
    swing vi.摇摆；回转 n.摇摆
    switch n.开关；转换 vt.转换
    swollen swell的过去分词
    symbol n.象征；符号,记号
    sympathetic a.同情的；和谐的
    sympathy n.同情；同感；慰问
    system n.系统,体系；制度
    table n.桌子
    tablet n.碑,匾；药片
    tackle vt.解决,对付 n.用具
    tail n.尾巴；尾部
    take v.拿,取；就座
    talk v.说话,谈话
    tall adj.高的
    tank n.水池；槽
    tap vt.&vi.&n.轻叩
    tape vt.系,捆
    target n.靶,标的；目标
    task n.任务,工作,作业
    taste vt.尝；尝到 n.味觉
    tax vt.抽税 n.税
    taxi n.出租汽车
    tea n.茶；茶叶；茶树
    teach vt.讲；教育 vt.教书
    teacher n.教师
    teaching n.教学,讲授；教导
    team vi.协作,合作
    tear vt.扯开,撕裂
    technical a.技术的,工艺的
    technique n.技术,技巧；技能
    technology n.工艺学,工艺,技术
    telephone n.电话 vi.打电话
    television n.电视；电视机
    tell v.告诉；讲述
    temperature n.温度
    temporarily ad. 暂时地
    temporary adj.暂时的；临时的
    tend vt. 护理；照料；照管,趋向；走向；照顾；vi. 倾向于；往往是；走向,趋向；服务；易于
    tendency n.趋向,趋势,倾向
    tension n. 紧张,不安,拉紧,电压,压力,
    tent n.帐篷
    term n.期；学期；条件；词
    terrible a.可怕的；极度的
    terribly adv. 可怕地；极坏地；厉害地；极
    test n.&vt.测验,考查
    text n.课文；课本
    than conj.比
    thank v.谢谢
    thanks n. 谢谢(只用复数)；谢意；感谢；int. 谢谢
    that a.那 pron.那 ad.那样
    The art.这(那)个；这些
    theatre n. 剧场,戏院； (阶梯式)教室；戏剧效果；舞台；剧院(theatre=theater)
    their pron.他(她、它)们的
    theirs pron.他(她)们的东西
    them pron.他(她)们,它们
    theme n.题目；词干；主旋律
    themselves pron.他们自己
    then adv.那么；然后
    theory n.理论；原理
    there adv.那儿
    therefore adv.因此；所以
    they pron.他们(她们,它们)
    thick adj.厚的；浓的
    thickly ad. 茂密地；葱葱地；厚厚地；密密地
    thickness n.厚(度)；密(度)
    thief n.窃贼,偷窃犯
    thin adj.瘦的
    thing n.事情,东西
    think vt.想；想要；认为
    thinking n. 思考；思想；见解
    thirsty adj.渴的；干燥的
    this pron.&adj.这,这个
    thorough a.彻底的；详尽的
    thoroughly adv. 彻底地；透彻地；充分地；完全地；全面地
    though conj.虽然 ad.可是
    thought n.思想；思维；想法
    thread n.线
    threat n.威胁,恐吓,凶兆
    threaten vt.&vi.威胁,恐吓
    threatening adj.胁迫的, 危险的
    throat n.喉咙
    through prep.穿过ad.从头到尾
    throughout prep.遍及
    throw vt.&vi.投掷；摔倒
    thumb n.(大)拇指
    Thursday n.星期四
    thus ad.如此,这样；因而
    ticket n.(交通违章)罚款传票
    tidy a.整洁的；整齐的
    tie vt.(用绳等)系,栓
    tight adv.紧紧地adj.牢固的
    tightly adv. 紧地；牢固地；紧紧地,紧密地
    till prep.conj.直到…为止
    time n.时间
    timetable n.时间表,时刻表
    tin n.锡；罐头
    tiny a.微小的,极小的
    tip n.梢,末端,尖,尖端
    tire vi.疲劳,累；厌倦
    tired adj.疲劳的,累的
    title n.标题,题目；称号
    to prep.到...
    today ad.在今天；现在
    toe n.脚趾,足尖
    together ad.共同,一起
    toilet n.厕所,盥洗室,浴室
    tomato n.番茄,西红柿
    tomorrow ad.在明天 n.明天
    ton n.吨(重量单位)
    tone n.色调,光度；风气
    tongue n.舌头；语言；口语
    tonight ad.在今夜 n.今夜
    tonne n. 公吨
    too adv.也
    tool n.工具；用具
    tooth n.牙齿
    top n.顶；首位 a.顶的
    topic n.(文章的)题目；主题
    total adj.总的 n.合计
    totally adv. 统统,完全地；全部地
    touch vt.触摸；接触
    tough a.坚韧的；健壮的
    tour n.&vi.旅行,游历
    tourist n.旅游者,观光者
    towards prep. 向,朝；对于；朝着；走向,近…；为了,有助于
    towel n.毛巾,手巾
    tower n.塔
    town n.镇,市镇,城镇
    toy n.玩具,玩物
    trace n.痕迹；丝毫 vt.跟踪
    track n.足迹；(火车的)轨道
    trade vi.经商,进行贸易
    tradition n.传统,惯例
    traditional a.传统的,惯例的
    traditionally ad. 世代相传地
    traffic n.交通,街道,车辆
    train n.火车
    training n.训练,锻炼,培养
    transfer vt.转移；调动vi.转移
    transform vt.改变；改造；变换
    translate vt.翻译,译 vt.翻译
    translation n.翻译；译文,译本
    transparent a.透明的；易识破的
    transport n.运输；运输工具
    trap vt.设陷阱捕捉；诱捕
    travel vi.&n.旅行
    traveller n. 旅客；旅行者
    treat vt.治疗
    treatment n.待遇；治疗,疗法
    tree n.树
    trend vi.伸向；倾向 n.倾向
    trial n.试,试验；审判
    triangle n.三角(形)
    trick n.诡计；计谋
    trip vi.绊；失足 vt .绊倒
    tropical a.热带的
    trouble n.烦恼；困难 vi.烦恼
    truck n.卡车
    true a.真的；忠实的
    truly adv.真正地,真实地
    trust vt.&n.信任
    truth n.真理；真相
    try vt.审问,审判
    tube n.管；电子管,显像管
    Tuesday n.星期二
    tune n.调子；和谐 vt.调谐
    tunnel n.隧道,坑道,地道
    turn v.翻；转
    TV n. 电视
    twice ad.两次,两倍
    twin a.孪生的 n.孪生儿
    twist vt.捻；拧 vi.&n.扭弯
    type n.类型；样式
    typical a.典型的,代表性的
    typically ad. 有代表性地
    tyre n.轮胎,车胎
    ugly adj.难看的
    ultimate a.最后的,最终的
    ultimately adv. 最后,终究；最终；终于
    umbrella n.伞
    unable adj.不能的,不会的
    unacceptable adj. 不能接受的
    uncertain a.无常的；不确定的
    uncle n.叔,伯,舅,姨父
    uncomfortable a.不舒服的；不自在的
    unconscious a.不省人事的
    under prep.在...下面
    underground adj.地下的
    underneath ad.在下面,在底下
    understand vt.懂；获悉 vi.懂得
    understanding n.理解；理解力；协定
    underwater a. 在水下的
    underwear n.衫衣,内衣,贴身衣
    undo vt.解开,打开；取消
    unemployed a. 失业的,未被利用的
    unemployment n.失业；失业人数
    unexpected a.想不到的,意外的
    unexpectedly ad. 出人意味地；意外地；突然地；未料到地
    unfair adj.不公平的
    unfortunate a.不幸的；可取的
    unfortunately adv. 不幸地,不凑巧；倒霉地；可惜；遗憾地；a. 使人遗憾的,不幸的
    unfriendly ad. 不友善地
    unhappiness n. 不幸福
    unhappy a.不幸福的,不快乐的
    uniform a.一样的 n.制服
    unimportant adj. 不重要的；琐碎的；平凡的；无价值的
    union n.联合；联合会,团结
    unique a.唯一的,独一无二的
    unit n.单位；单元；部件
    unite n. 联合,统一,合并,(使)一致行动；vi. 统一；联合；vt. 使联合；使结合
    united adj. 统一的；联合的
    universe n.宇宙,世界
    university n.综合性大学
    unkind a.不仁慈的,不和善的
    unknown adj.不为人所知的
    unless conj.除非,如果不
    unlike a.不同的 prep.不象…
    unlikely a.未必的,未必可能的
    unload vt.从...卸下货物
    unlucky a.不幸的；不吉的
    unnecessary a.不必要的,多余的
    unpleasant a.令人不快的,讨厌的
    unreasonable a.不讲道理的；过度的
    unsteady adj. 不安定的,不稳的; 摇晃的
    unsuccessful a. 不成功的,失败的
    untidy a. 不整齐的,零乱的
    until conj.直到...为止
    unusual adj.不常见的；奇异的
    unusually a. 不平常地,非常；ad. 异常地；非常
    unwilling a.不愿意的
    unwillingly ad. 不情愿地,勉强地
    up ad.向上；起床,起来
    upon prep.在...上面
    upper a.上面的；地位较高的
    upset adj.难过的；不安的
    upside n.上部；上边
    upstairs adv.在楼上adj.楼上的
    upward adv.向上
    upwards adv. 向上；趋向上升；以上；(同)upward
    urban a. 城市的
    urge vt.激励；催促
    urgent a.紧急的；强求的
    us pron.(宾格)我们
    use vt.用；耗费 n.用
    used vi.过去常常
    useful adj.有用的；有益的
    useless a.无用的,无价值的
    user n.用户,使用者
    usual adj.通常的；平常的
    usually adv.通常
    vacation n.假期,休假
    valid a.有效的；正当的
    valley n.流域；(山)谷
    valuable n.贵重物品,财宝
    value vt.尊重,重视,评价
    van n.大篷车,运货车
    variation n.变化,变动；变异
    varied adj. 不同的；各种各样的
    variety n.多样化；种类；变种
    various a.各种各样的,不同的
    vary vt.改变；使多样化
    vast a.巨大的；大量的
    vegetable n.植物；蔬菜
    vehicle n.车辆,机动车
    venture n.&vi.冒险 vt.敢于
    version n.译文；说法；改写本
    vertical a.垂直的,竖式的
    very ad.很；完全 a.真的
    via prep.经过；通过
    victim n.牺牲者,受害者
    victory n.胜利
    video a.录象的
    view n.视域
    village n.乡村,村庄
    violence n.猛烈,激烈；暴力
    violent a.猛烈的；狂暴的
    violently ad. 猛烈地；剧烈地；凶暴地；强暴地
    virtually ad. 实际上,事实上；实质上；几乎；adj. 几乎,差不多
    virus n. 病毒
    visible a.可见的,看得见的
    vision n.视力；眼光,想象力
    visit vt.常去
    visitor n.访问者；参观者
    vital a.生命的,生机的
    vocabulary n.词汇表,词汇汇编
    voice n.说话声；意见；语态
    volume n.卷,册；容积；音量
    vote n.选举,投票,表决
    wage n.工资,报酬
    waist n.腰,腰部
    wait vi.等,等候 n.等待
    waiter n.侍者(服务员)
    wake v.醒
    walk vi.&n.走,步行
    wall n.墙,壁,围墙,城墙
    wallet n.钱夹；皮夹
    wander vi.徘徊；流浪vt.漫游
    want vt.要,想要；需要
    war n.战争；冲突,斗争
    warm adj.暧和的
    warmth n.暖和,温暖；热烈
    warn vt.警告,告诫
    warning n.警告,告诫,鉴诫
    wash vt.洗；冲出 vi.洗涤
    washing n. 洗；洗的
    waste n.&vt.浪费
    watch n.手表
    water n.水
    wave n.波,波浪；波动
    way n.路；路线；方向
    we pron.(主格)我们
    weak a.弱的；软弱的
    weakness n.虚弱,软弱；弱点
    wealth n.财富,财产；丰富
    weapon n.武器,兵器
    wear vt.穿,戴
    weather n.天气
    web n.网,丝,网状物
    wedding n.婚礼
    Wednesday n.星期三
    week n.星期,周
    weekend n.周末,周末假期
    weekly a.每周的 ad.每周
    weigh vi. 重(若干)；权衡；vt. 称…的重量；掂量；称量；认真考虑
    weight n.重；砝码；重担
    welcome int.&n.&vt.欢迎
    well n.井；泉水；深坑
    west n.西部,西方
    western adj.西的,西方的
    wet adj.湿的
    what pron.&adj.什么
    whatever adj.&pron.无论什么
    wheel n.轮,车轮
    when ad.什么时候；当…时
    whenever conj. & adv. 随时；无论何时；无论什么时候,每当
    where adv.在哪里
    whereas conj.而,却,反之
    wherever adv.无论在(到)哪里
    whether conj.是否
    which pron.哪一个
    while conj.当...的时候
    whilst conj.同…同时；然而
    whisper vt.低声地讲,私下说
    whistle n.口哨声 vi.打口哨
    white adj.白色的
    who pron.谁；…的人
    whoever pron.究竟是谁
    whole adj.整个的
    whom pron.谁(宾格)
    whose pron.谁的；哪个人的
    why ad.为什么
    wide adv.广阔地；充分地
    widely adv.广阔地；广泛地
    width n.宽阔,广阔；宽度
    wife n.妻子
    wild a.野生的；野蛮的
    wildly adv. 暴风雨般地；疯狂地,急切地；发狂地,荒唐地
    will v.aux.将；会；愿
    willing adj.甘心情愿的
    willingly adv. 乐意地,自愿地；情愿地
    willingness n. 自动自发
    win vi.获胜 vt.赢得
    wind n.风
    window n.窗子,窗户,窗口
    wine n.酒
    wing n.翅膀
    winner n.获胜者,优胜者
    winning n. & a. 胜利(的)
    winter n.冬天,冬季
    wire n.(金属)线；电线
    wise adj.有智慧的,聪明的
    wish vt.&n.希望；祝愿
    with prep.带有
    withdraw vt.收回；撤回vi.撤退
    within prep. 在…里面；在…范围之内；不超过；在…以内；adv. 在里面,在内部
    without prep.无,没有,不
    witness n.证据；证人 vt.目击
    woman n.妇女,女人
    wonder n.惊异,惊奇；奇迹
    wonderful adj.极好的,精彩的
    wood n.树林
    wooden adj.木制的
    wool n.羊毛；毛线,绒线
    word n.词,单词
    work v.&n.工作
    worker n.工人
    working a. 工人的；劳动的；n. 工作,操作,作业；劳动的
    world n.世界
    worried adj. 焦虑的；烦恼的；担心的；忧心忡忡的；担忧的；焦急的
    worry vt.(使)担忧
    worse adj.更坏的,更差的
    worship vt.崇拜 vi.做礼拜
    worth adj.值得...的
    would aux.v.将；愿；总是
    wound n.创伤,伤 vt.使受伤
    wounded adj. 受伤的；n. 伤员
    wrap vt.裹,包,捆 n.披肩
    wrapping n. (pl.)包装材料
    wrist n.手腕
    write vt.书写；写 vi.写
    writer n.作者,作家,文学家
    writing n.书写,写；著作
    written adj. 写作的,书面的；write的过去分词
    wrong a.错误的 ad.错,不对
    wrongly adv. 错误地,不正当地
    yard n.码(英美长度单位)
    yawn vi.打呵欠 n.呵欠
    yeah ad. (口)(同)yes
    year n.年；年年
    yellow adj.黄色的
    yes adv.是,是的
    yesterday n.&ad.昨天,昨日
    yet adv.仍然
    you pron.你,你们
    young adj.年青的
    your pron.你的,你们的
    Yours pron.你们的(东西)
    yourself pron.你自己；你亲自
    youth n.青年
    zero n.零；零点,零度
    zone n.地区,区域,范围'''
    text_to_python_dir(text)