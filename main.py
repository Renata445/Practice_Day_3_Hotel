from sqlalchemy import create_engine, Column, Integer, String, text, ForeignKey, DATE
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped, Session


engine = create_engine("mysql+mysqlconnector://root:1234@localhost:3306")

connection = engine.connect()

connection.execute(text("DROP DATABASE IF EXISTS hotel"))
connection.execute(text("CREATE DATABASE IF NOT EXISTS hotel"))

engine = create_engine("mysql+mysqlconnector://root:1234@localhost/hotel")
connection = engine.connect()


class Base(DeclarativeBase):
    pass


class class_t(Base):
    __tablename__ = 'class'

    id_class: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)


class staff_t(Base):
    __tablename__ = 'staff'

    id_staff: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[str] = mapped_column(String(32), nullable=False)
    name: Mapped[str] = mapped_column(String(32), nullable=False)
    phone: Mapped[str] = mapped_column(String(32), nullable=False)

class rooms_t(Base):
    __tablename__ = 'rooms'

    id_room: Mapped[int] = mapped_column(primary_key=True)
    number_of_places: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False)
    class_id: Mapped[int] = mapped_column(Integer, ForeignKey("class.id_class"))


class room_service_t(Base):
    __tablename__ = 'room_service'

    id_room_service: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(Integer, ForeignKey("rooms.id_room"))
    staff_id: Mapped[int] = mapped_column(Integer, ForeignKey("staff.id_staff"))

class guests_t (Base):
    __tablename__ = 'guests'

    id_guests: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[str] = mapped_column(String(32), nullable=False)
    name: Mapped[str] = mapped_column(String(32), nullable=False)
    passport: Mapped[int] = mapped_column(String(32), nullable=False)
    check_in: Mapped[DATE] = mapped_column(DATE, nullable=False)
    check_out: Mapped[DATE] = mapped_column(DATE, nullable=False)
    room_id: Mapped[int] = mapped_column(Integer, ForeignKey("rooms.id_room"))

Base.metadata.create_all(bind=engine)

class session_add(Base):
    with Session(autoflush=False, bind=engine) as hotel:
        Staff1 = staff_t(id_staff=1, surname='Varinova', name='Natasha', phone='+799566781')
        Staff2 = staff_t(id_staff=2, surname='Fortunov', name='Georgiy', phone='+798756222')
        Staff3 = staff_t(id_staff=3, surname='Postanov', name='Oleg', phone='+799399993')
        Staff4 = staff_t(id_staff=4, surname='Gatin', name='Dima', phone='+799490094')
        Staff5 = staff_t(id_staff=5, surname='Bulatov', name='Yana', phone='+799955695')
        Staff6 = staff_t(id_staff=6, surname='Agmalova', name='Renata', phone='+799699996')
        Staff7 = staff_t(id_staff=7, surname='Dudkin', name='Denis', phone='+796789997')
        Staff8 = staff_t(id_staff=8, surname='Gavrilina', name='Julia', phone='+799236798')
        Staff9 = staff_t(id_staff=9, surname='Stanislavovna', name='Karina', phone='+799178999')
        Staff10 = staff_t(id_staff=10, surname='Djenner', name='Stormi', phone='+79999004310')
        hotel.add(Staff1)
        hotel.add(Staff2)
        hotel.add(Staff3)
        hotel.add(Staff4)
        hotel.add(Staff5)
        hotel.add(Staff6)
        hotel.add(Staff7)
        hotel.add(Staff8)
        hotel.add(Staff9)
        hotel.add(Staff10)
        hotel.commit()
connection.commit()



