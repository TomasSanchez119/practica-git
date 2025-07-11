#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
from config import Config

def test_database_connection():
    """Prueba la conexión a la base de datos y las tablas"""
    try:
        # Conectar a la base de datos
        connection = pymysql.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            cursorclass=pymysql.cursors.DictCursor
        )
        
        print("✅ Conexión a la base de datos exitosa")
        
        with connection.cursor() as cursor:
            # Verificar que las tablas existan
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            print(f"📋 Tablas encontradas: {len(tables)}")
            
            for table in tables:
                table_name = list(table.values())[0]
                print(f"  - {table_name}")
            
            # Verificar estructura de la tabla albumes
            cursor.execute("DESCRIBE albumes")
            albumes_structure = cursor.fetchall()
            print("\n📊 Estructura de la tabla 'albumes':")
            for field in albumes_structure:
                print(f"  - {field['Field']}: {field['Type']}")
            
            # Verificar estructura de la tabla musica
            cursor.execute("DESCRIBE musica")
            musica_structure = cursor.fetchall()
            print("\n🎵 Estructura de la tabla 'musica':")
            for field in musica_structure:
                print(f"  - {field['Field']}: {field['Type']}")
            
            # Verificar estructura de la tabla albumes_musica
            cursor.execute("DESCRIBE albumes_musica")
            albumes_musica_structure = cursor.fetchall()
            print("\n🔗 Estructura de la tabla 'albumes_musica':")
            for field in albumes_musica_structure:
                print(f"  - {field['Field']}: {field['Type']}")
            
            # Contar registros en cada tabla
            cursor.execute("SELECT COUNT(*) as count FROM albumes")
            albumes_count = cursor.fetchone()['count']
            print(f"\n📈 Registros en 'albumes': {albumes_count}")
            
            cursor.execute("SELECT COUNT(*) as count FROM musica")
            musica_count = cursor.fetchone()['count']
            print(f"🎵 Registros en 'musica': {musica_count}")
            
            cursor.execute("SELECT COUNT(*) as count FROM albumes_musica")
            albumes_musica_count = cursor.fetchone()['count']
            print(f"🔗 Registros en 'albumes_musica': {albumes_musica_count}")
        
        connection.close()
        print("\n✅ Prueba completada exitosamente")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("🔍 Probando conexión a la base de datos...")
    test_database_connection() 