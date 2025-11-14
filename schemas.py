from datetime import datetime, date
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


# -------------------------------------------
# BIBLIOTECA
# -------------------------------------------


class BibliotecaBase(BaseModel):
    nombre: str
    id_sede: UUID


class BibliotecaCreate(BibliotecaBase):
    pass


class BibliotecaUpdate(BaseModel):
    nombre: Optional[str] = None
    id_sede: Optional[UUID] = None


class SedeResponse(BaseModel):
    id_sede: UUID
    nombre: Optional[str] = None


class BibliotecaResponse(BibliotecaBase):
    id_biblioteca: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None
    sede: Optional[SedeResponse] = None

    class Config:
        from_attributes = True


# -------------------------------------------
# CATEGORIA
# -------------------------------------------


class CategoriaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    id_biblioteca: UUID


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    id_biblioteca: Optional[UUID] = None


class BibliotecaSimpleResponse(BaseModel):
    id_biblioteca: UUID
    nombre: str


class CategoriaResponse(CategoriaBase):
    id_categoria: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None
    biblioteca: Optional[BibliotecaSimpleResponse] = None

    class Config:
        from_attributes = True


# -------------------------------------------
# CLIENTE
# -------------------------------------------


class ClienteBase(BaseModel):
    nombre: str
    tipo_cliente: str
    detalle_tipo: str
    vetado: bool
    id_biblioteca: UUID


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    tipo_cliente: Optional[str] = None
    detalle_tipo: Optional[str] = None
    vetado: Optional[bool] = None
    id_biblioteca: Optional[UUID] = None


class BibliotecaSimpleResponse(BaseModel):
    id_biblioteca: UUID
    nombre: str


class ClienteResponse(ClienteBase):
    codigo: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None
    biblioteca: Optional[BibliotecaSimpleResponse] = None

    class Config:
        from_attributes = True


# -------------------------------------------
# MATERIAL BIBLIOGRAFICO
# -------------------------------------------


class Material_BibliograficoBase(BaseModel):
    titulo: str
    autor: str
    estado: str
    id_biblioteca: UUID
    id_categoria: UUID
    id_sede: UUID


class Material_BibliograficoCreate(Material_BibliograficoBase):
    pass


class Material_BibliograficoUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    estado: Optional[str] = None
    id_biblioteca: Optional[UUID] = None
    id_categoria: Optional[UUID] = None
    id_sede: Optional[UUID] = None


class BibliotecaSimpleResponse(BaseModel):
    id_biblioteca: UUID
    nombre: str


class CategoriaSimpleResponse(BaseModel):
    id_categoria: UUID
    nombre: str


class Material_BibliograficoResponse(Material_BibliograficoBase):
    id_material: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None
    biblioteca: Optional[BibliotecaSimpleResponse] = None
    categoria: Optional[CategoriaSimpleResponse] = None

    class Config:
        from_attributes = True


# -------------------------------------------
# PRESTAMO
# -------------------------------------------
class PrestamoBase(BaseModel):
    fecha_prestamo: date
    fecha_entrega: date
    id_biblioteca: UUID
    id_material: UUID
    cod_cliente: UUID


class PrestamoCreate(PrestamoBase):
    pass


class PrestamoUpdate(BaseModel):
    fecha_prestamo: Optional[date] = None
    fecha_entrega: Optional[date] = None
    id_material: Optional[UUID] = None
    cod_cliente: Optional[UUID] = None
    id_biblioteca: Optional[UUID] = None


class BibliotecaResponseMini(BaseModel):
    nombre: str


class MaterialResponseMini(BaseModel):
    titulo: str


class ClienteResponseMini(BaseModel):
    nombre: str


class PrestamoResponse(PrestamoBase):
    id: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None
    biblioteca: Optional[BibliotecaResponseMini] = None
    material: Optional[MaterialResponseMini] = None
    cliente: Optional[ClienteResponseMini] = None

    class Config:
        from_attributes = True


# -------------------------------------------
# RESERVA
# -------------------------------------------
class ReservaBase(BaseModel):
    fecha_reserva: date
    estado: str
    cod_cliente: UUID
    id_material: UUID
    id_biblioteca: UUID


class ReservaCreate(ReservaBase):
    pass


class ReservaUpdate(BaseModel):
    fecha_reserva: Optional[date] = None
    estado: Optional[str] = None
    cod_cliente: Optional[UUID] = None
    id_material: Optional[UUID] = None
    id_biblioteca: Optional[UUID] = None


class BibliotecaResponseMini(BaseModel):
    nombre: str


class ClienteResponseMini(BaseModel):
    nombre: str


class MaterialResponseMini(BaseModel):
    titulo: str


class ReservaResponse(ReservaBase):
    id_reserva: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None
    biblioteca: Optional[BibliotecaResponseMini] = None
    cliente: Optional[ClienteResponseMini] = None
    material: Optional[MaterialResponseMini] = None

    class Config:
        from_attributes = True


# -------------------------------------------
# SANCION
# -------------------------------------------
class SancionBase(BaseModel):
    fecha_sancion: date
    monto: float
    motivo: str
    cod_cliente: UUID
    id_biblioteca: UUID


class SancionCreate(SancionBase):
    pass


class SancionUpdate(BaseModel):
    fecha_sancion: Optional[date] = None
    motivo: Optional[str] = None
    monto: Optional[float] = None


class BibliotecaResponseMini(BaseModel):
    nombre: str


class ClienteResponseMini(BaseModel):
    nombre: str


class SancionResponse(SancionBase):
    id_sancion: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None
    biblioteca: Optional[BibliotecaResponseMini] = None
    cliente: Optional[ClienteResponseMini] = None

    class Config:
        from_attributes = True


# -------------------------------------------
# SEDE
# -------------------------------------------
class SedeBase(BaseModel):
    nombre: str
    direccion: str


class SedeCreate(SedeBase):
    pass


class SedeUpdate(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None


class SedeResponse(SedeBase):
    id_sede: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None

    class Config:
        from_attributes = True


# -------------------------------------------
# USUARIO
# -------------------------------------------
class UsuarioBase(BaseModel):
    nombre: str
    nombre_usuario: str
    email: EmailStr
    telefono: Optional[str] = None
    es_admin: bool = False


class UsuarioCreate(UsuarioBase):
    contraseña: str


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    nombre_usuario: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    es_admin: Optional[bool] = None
    activo: Optional[bool] = None


class UsuarioResponse(UsuarioBase):
    id_usuario: UUID
    activo: bool
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None

    class Config:
        from_attributes = True


class UsuarioLogin(BaseModel):
    nombre_usuario: str
    contraseña: str


class CambioContraseña(BaseModel):
    contraseña_actual: str
    nueva_contraseña: str


# Modelos de respuesta con relaciones
class CategoriaConMateriales(CategoriaResponse):
    materiales: List[Material_BibliograficoResponse] = []


class BibliotecaConRelaciones(BibliotecaResponse):
    categorias: List[CategoriaResponse] = []
    clientes: List[ClienteResponse] = []
    materiales: List[Material_BibliograficoResponse] = []


class ClienteConRelaciones(ClienteResponse):
    prestamos: List[PrestamoResponse] = []
    reservas: List[ReservaResponse] = []
    sanciones: List[SancionResponse] = []


class MaterialConRelaciones(Material_BibliograficoResponse):
    prestamos: List[PrestamoResponse] = []
    reservas: List[ReservaResponse] = []


# Relaciones para Préstamo
class PrestamoConRelaciones(PrestamoResponse):
    cliente: ClienteResponse
    material: Material_BibliograficoResponse
    usuario: UsuarioResponse


# Relaciones para Reserva
class ReservaConRelaciones(ReservaResponse):
    cliente: ClienteResponse
    material: Material_BibliograficoResponse
    usuario: UsuarioResponse


# Relaciones para Sanción
class SancionConRelaciones(SancionResponse):
    cliente: ClienteResponse
    usuario: UsuarioResponse


# Relaciones para Sede
class SedeConRelaciones(SedeResponse):
    bibliotecas: List[BibliotecaResponse] = []


# Ampliación de Usuario con todas las acciones posibles
class UsuarioConAcciones(UsuarioResponse):
    bibliotecas_creadas: List[BibliotecaResponse] = []
    categorias_creadas: List[CategoriaResponse] = []
    materiales_creados: List[Material_BibliograficoResponse] = []
    clientes_creados: List[ClienteResponse] = []
    prestamos_registrados: List[PrestamoResponse] = []
    reservas_registradas: List[ReservaResponse] = []
    sanciones_registradas: List[SancionResponse] = []


# Modelos de respuesta para la API


class RespuestaAPI(BaseModel):
    mensaje: str
    exito: bool = True
    datos: Optional[dict] = None


class RespuestaError(BaseModel):
    mensaje: str
    exito: bool = False
    error: str
    codigo: int
