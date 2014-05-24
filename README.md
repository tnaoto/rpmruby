How to use
====

イメージ作成
-----
```
docker build -t 'rpm/ruby' .
```

rubyのビルド
----
```
docker run -v ./build:/rpmbuild/RPMS:rw  -t rpm/ruby
```

余談
----
絶対パスじゃないとダメっぽい気がする

```
docker run -v /root/rpmruby:/rpmbuild  -t rpm/ruby
docker run -v /root/rpmruby/build:/rpmbuild/RPMS/x86_64/  -t rpm/ruby
```
