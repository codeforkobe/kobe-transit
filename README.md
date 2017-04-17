GTFS
====
神戸市地下鉄の [GTFS](https://developers.google.com/transit/gtfs/reference) 
形式ファイル `kobe_subway_gtfs.zip` を作成します。

GTFS 拡張仕様の多言語（multilingual）対応を使います。
https://support.google.com/transitpartners/answer/2450962


Requirement
-----------
+ make
+ python3
+ wget


License
-------
GTFS ファイルは [CC-BY-SA](http://creativecommons.org/licenses/by-sa/3.0/) でライセンスします。
+ 時刻表・駅情報は神戸市による [CC-BY](http://creativecommons.org/licenses/by/2.1/jp/) ライセンス適用です。
+ 緯度経度情報は Wikipedia(dbpedia) による [CC-BY-SA](http://creativecommons.org/licenses/by-sa/3.0/) ライセンス適用です。

プログラムは [Apache license 2.0](http://www.apache.org/licenses/LICENSE-2.0) でライセンスします。


Feeds
-----
- Transit.land [registered](https://transit.land/feed-registry/operators/o-xn0j-kobe)
- TransitFeeds [requesting](https://github.com/TransitFeeds/TransitFeeds-Public/issues/125)

参考文献
========
- 国土交通省 [標準的なバス情報フォーマット](https://twitter.com/MLIT_JAPAN/status/847745529450700801)
- [（翻訳）公共交通データは誰のものか？](http://niyalist.hatenablog.com/entry/2017/04/15/121315)
- 012050 [道南バスGTFS化プロジェクト](https://github.com/aruneko/DonanBusGTFS)
- 172111 [能美市コミュニティバス時刻表及び経路GTFSデータ](http://www.city.nomi.ishikawa.jp/chiiki/NomiVitalization/opendata.html)

- 182079 http://www.city.sabae.fukui.jp/users/tutujibus/web-api/web-api.html
- 232157 http://www.city.inuyama.aichi.jp/shisei/toukei/1003763.html
- 252069 http://www.city.kusatsu.shiga.jp/kurashi/kotsudorokasen/mamebus/opendata.html
- 261009 https://data.city.kyoto.lg.jp/node/14553

- http://opentrans.it/#/aboutus
