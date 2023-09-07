"""
from django.test import TransactionTestCase, Client
from apps.func.models.funcionalidades import Cliente, RegistroFactura, ItemFactura, RegistroCredito, AbonosCredito, InventarioMaquinaria
from rest_framework import status
from apps.users.models.user import User


class ClienteViewSetTestCase(TransactionTestCase):

    def setUp(self):
        self.client = Client()
        
        # User Data for Authentication
        self.user_data = {
            "email": "test@test.com",
            "username": "testuser",
            "full_name": "Test User",
            "password": "testpassword123"
        }
        self.user = User.objects.create_user(**self.user_data)
        self.login_data = {
            "email": "test@test.com",
            "password": "testpassword123"
        }
        login_response = self.client.post('/auth/login/', self.login_data)
        self.token = login_response.data['access']
        
        # Cliente Data
        self.cliente_data = {
            "nombre": "Cliente Test",
            "identificacion": "123456789",
            "direccion": "Calle 123",
            "telefono": "3001234567",
            "correo": "cliente@test.com",
            "fecha_registro": "2023-09-05",
            "estado": "ACTIVO",
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.cliente = Cliente.objects.create(**self.cliente_data)

    def test_list_clientes(self):
        response = self.client.get('/clientes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_cliente_success(self):
        response = self.client.post('/clientes/', self.cliente_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Cliente.objects.filter(nombre="Cliente Test").exists())

    def test_create_cliente_invalid_data(self):
        invalid_data = {
            "nombre": "",  # Empty name
            "identificacion": "123456789",
            "direccion": "Calle 123",
            "telefono": "3001234567",
            "correo": "cliente@test.com",
            "fecha_registro": "2023-09-05",
            "estado": "ACTIVO",
        }
        response = self.client.post('/clientes/', invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_cliente(self):
        response = self.client.get(f'/clientes/{self.cliente.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Cliente Test")

    def test_delete_cliente(self):
        response = self.client.delete(f'/clientes/{self.cliente.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Cliente.objects.filter(id=self.cliente.id).exists())



class RegistroCreditoViewSetTestCase(TransactionTestCase):

    def setUp(self):
        self.client = Client()
        
        # User Data for Authentication
        self.user_data = {
            "email": "test@test.com",
            "username": "testuser",
            "full_name": "Test User",
            "password": "testpassword123"
        }
        self.user = User.objects.create_user(**self.user_data)
        self.login_data = {
            "email": "test@test.com",
            "password": "testpassword123"
        }
        login_response = self.client.post('/auth/login/', self.login_data)
        self.token = login_response.data['access']
        
        # Cliente Data (Already provided, just referencing here)
        self.cliente = Cliente.objects.create(**self.cliente_data)
        
        # RegistroCredito Data
        self.credito_data = {
            "cliente": self.cliente.id,
            "fecha": "2023-09-05",
            "valor_total": 5000,
            "estado": "PENDIENTE",
            "saldo_pendiente": 2500
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.credito = RegistroCredito.objects.create(**self.credito_data)

    def test_list_creditos(self):
        response = self.client.get('/creditos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_credito_success(self):
        response = self.client.post('/creditos/', self.credito_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(RegistroCredito.objects.filter(cliente=self.cliente).exists())

    def test_create_credito_invalid_data(self):
        invalid_data = {
            "cliente": self.cliente.id,
            "fecha": "",
            "valor_total": "",
            "estado": "PENDIENTE",
            "saldo_pendiente": ""
        }
        response = self.client.post('/creditos/', invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_credito(self):
        response = self.client.get(f'/creditos/{self.credito.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "PENDIENTE")

    def test_delete_credito(self):
        response = self.client.delete(f'/creditos/{self.credito.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(RegistroCredito.objects.filter(id=self.credito.id).exists())



class AbonosCreditoViewSetTestCase(TransactionTestCase):

    def setUp(self):
        self.client = Client()
        
        # User Data for Authentication
        self.user_data = {
            "email": "test@test.com",
            "username": "testuser",
            "full_name": "Test User",
            "password": "testpassword123"
        }
        self.user = User.objects.create_user(**self.user_data)
        self.login_data = {
            "email": "test@test.com",
            "password": "testpassword123"
        }
        login_response = self.client.post('/auth/login/', self.login_data)
        self.token = login_response.data['access']
        
        # Cliente Data (Already provided, just referencing here)
        self.cliente = Cliente.objects.create(**self.cliente_data)
        
        # RegistroCredito Data (Already provided, just referencing here)
        self.credito = RegistroCredito.objects.create(**self.credito_data)
        
        # AbonosCredito Data
        self.abono_data = {
            "credito": self.credito.id,
            "fecha": "2023-09-05",
            "valor": 1000,
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.abono = AbonosCredito.objects.create(**self.abono_data)

    def test_list_abonos(self):
        response = self.client.get('/abonos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_abono_success(self):
        response = self.client.post('/abonos/', self.abono_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(AbonosCredito.objects.filter(credito=self.credito).exists())

    def test_create_abono_invalid_data(self):
        invalid_data = {
            "credito": self.credito.id,
            "fecha": "",
            "valor": "",
        }
        response = self.client.post('/abonos/', invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_abono(self):
        response = self.client.get(f'/abonos/{self.abono.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, str(self.abono.valor))

    def test_delete_abono(self):
        response = self.client.delete(f'/abonos/{self.abono.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(AbonosCredito.objects.filter(id=self.abono.id).exists())



class InventarioMaquinariaViewSetTestCase(TransactionTestCase):

    def setUp(self):
        self.client = Client()
        
        # User Data for Authentication
        self.user_data = {
            "email": "test@test.com",
            "username": "testuser",
            "full_name": "Test User",
            "password": "testpassword123"
        }
        self.user = User.objects.create_user(**self.user_data)
        self.login_data = {
            "email": "test@test.com",
            "password": "testpassword123"
        }
        login_response = self.client.post('/auth/login/', self.login_data)
        self.token = login_response.data['access']
        
        # InventarioMaquinaria Data
        self.inventario_data = {
            "nombre": "Excavadora",
            "descripcion": "Excavadora de gran tamaño",
            "fecha_registro": "2023-09-05",
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.inventario = InventarioMaquinaria.objects.create(**self.inventario_data)

    def test_list_inventarios(self):
        response = self.client.get('/inventarios/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_inventario_success(self):
        response = self.client.post('/inventarios/', self.inventario_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(InventarioMaquinaria.objects.filter(nombre="Excavadora").exists())

    def test_create_inventario_invalid_data(self):
        invalid_data = {
            "nombre": "",
            "descripcion": "Excavadora de gran tamaño",
            "fecha_registro": "2023-09-05",
        }
        response = self.client.post('/inventarios/', invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_inventario(self):
        response = self.client.get(f'/inventarios/{self.inventario.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Excavadora")

    def test_delete_inventario(self):
        response = self.client.delete(f'/inventarios/{self.inventario.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(InventarioMaquinaria.objects.filter(id=self.inventario.id).exists())



class ItemFacturaViewSetTestCase(TransactionTestCase):

    def setUp(self):
        self.client = Client()
        
        # User Data for Authentication
        self.user_data = {
            "email": "test@test.com",
            "username": "testuser",
            "full_name": "Test User",
            "password": "testpassword123"
        }
        self.user = User.objects.create_user(**self.user_data)
        self.login_data = {
            "email": "test@test.com",
            "password": "testpassword123"
        }
        login_response = self.client.post('/auth/login/', self.login_data)
        self.token = login_response.data['access']
        
        # Cliente Data (Already provided, just referencing here)
        self.cliente = Cliente.objects.create(**self.cliente_data)
        
        # RegistroFactura Data (Already provided, just referencing here)
        self.factura = RegistroFactura.objects.create(**self.factura_data)
        
        # ItemFactura Data
        self.item_data = {
            "factura": self.factura.id,
            "descripcion": "Excavadora",
            "valor_unitario": 5000,
            "cantidad": 2,
            "valor_total": 10000
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.item = ItemFactura.objects.create(**self.item_data)

    def test_list_items(self):
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_item_success(self):
        response = self.client.post('/items/', self.item_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(ItemFactura.objects.filter(descripcion="Excavadora").exists())

    def test_create_item_invalid_data(self):
        invalid_data = {
            "factura": self.factura.id,
            "descripcion": "",
            "valor_unitario": "",
            "cantidad": "",
            "valor_total": ""
        }
        response = self.client.post('/items/', invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_item(self):
        response = self.client.get(f'/items/{self.item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Excavadora")
"""