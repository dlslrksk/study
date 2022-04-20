# sql 모듈 생성
# Class 생성 (Database)
# Class가 생성이 될 때, pymysql.connect 변수 및 cursor 생성(__init__)
# init을 제외한 함수 생성
# execute() >> _sql, _values를 인자로 받아와서 sql문 실행
# executeAll() >> _sql, _values를 인자로 받아와서 sql문 실행 후 결과값 return
# commit() >> commit을 하는 함수
# execute(), executeAll()함수에서 value 값은 디폴트 {}값 지정
# main.py에 모듈을 load해서 기존 sql 작업을 사용해서 코드 작성

from flask import Flask, redirect, render_template, request, redirect, url_for
import pymysql

class Database():
    def __init__(self):
        self._db = pymysql.connect(
        user = 'root',
        passwd = 'dbtjr2293!',
        host = 'localhost',
        db = 'ubion',
        charset = 'utf8'
        )

        self.cursor = self._db.cursor(pymysql.cursors.DictCursor)

    def execute(self, _sql, _values={}):
        self.cursor.execute(_sql, _values)

    def executeAll(self, _sql, _values={}):
        self.cursor.execute(_sql, _values)
        self.result = self.cursor.fetchall()

        return self.result

    def commit(self):
        self._db.commit()