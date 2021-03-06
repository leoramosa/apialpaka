# Generated by Django 3.0.8 on 2020-10-08 16:06

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrecategoria', models.CharField(blank=True, max_length=200, null=True)),
                ('photo_category_product', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('fotocategoria', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('fotocategoria1', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('fotocategoria2', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('fotocategoria3', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('fotocategoria4', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('imagen', models.CharField(blank=True, max_length=200, null=True)),
                ('activo', models.IntegerField()),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'categoria',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomcliente', models.CharField(db_column='nomCliente', max_length=200)),
                ('direccliente', models.CharField(blank=True, db_column='direcCliente', max_length=200, null=True)),
                ('ruc', models.CharField(blank=True, db_column='RUC', max_length=11, null=True)),
                ('fechanac', models.DateField(blank=True, db_column='fechaNac', null=True)),
                ('telefono1', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono2', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono3', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrecolor', models.CharField(blank=True, db_column='nombreColor', max_length=60, null=True)),
                ('numbercolor', models.CharField(blank=True, db_column='numberColor', max_length=60, null=True)),
                ('valuecolor', models.CharField(blank=True, db_column='valuColor', max_length=60, null=True)),
                ('imagencolor1', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('imagencolor2', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('imagencolor3', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('imagencolor4', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('imagencolor5', models.ImageField(blank=True, null=True, upload_to='productos')),
            ],
            options={
                'db_table': 'nombrecolor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomgenero', models.CharField(db_column='nomGenero', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nommarca', models.CharField(db_column='nomMarca', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nommodelo', models.CharField(blank=True, db_column='nomModelo', max_length=60, null=True)),
                ('descmodelo', models.CharField(blank=True, db_column='descModelo', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('fotoportadaactivo', models.IntegerField(blank=True, null=True)),
                ('fotoportada', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('fotoprincipal', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('cantidadstock', models.CharField(blank=True, db_column='CantidadStock', max_length=100, null=True)),
                ('precionormal', models.IntegerField(blank=True, db_column='PrecioNormal', null=True)),
                ('preciointernet', models.IntegerField(blank=True, db_column='PrecioInternet', null=True)),
                ('preciopromocion', models.IntegerField(blank=True, db_column='PrecioPromocion', null=True)),
                ('preciooferta', models.IntegerField(blank=True, db_column='ProdOferta', null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('brevedescripcion', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
                ('mostrarpaginicio', models.IntegerField(blank=True, null=True)),
                ('activo', models.IntegerField(blank=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('state', models.BooleanField(blank=True, default=True, null=True)),
                ('idcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Categoria')),
                ('idcolor', models.ManyToManyField(to='servicios.Color')),
                ('idgenero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Genero')),
                ('idmarca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Marca')),
                ('idmodelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Modelo')),
            ],
            options={
                'db_table': 'producto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomtalla', models.CharField(blank=True, db_column='nomTalla', max_length=60, null=True)),
                ('numtalla', models.IntegerField(blank=True, db_column='NumTalla', null=True)),
                ('value', models.CharField(blank=True, db_column='numvalue', max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipopago',
            fields=[
                ('idtipopago', models.IntegerField(db_column='idTipoPago', primary_key=True, serialize=False)),
                ('nomtipopago', models.CharField(db_column='nomTipoPago', max_length=50)),
            ],
            options={
                'db_table': 'tipopago',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tipoproducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomtipoproducto', models.CharField(db_column='nomTipoProducto', max_length=60)),
            ],
            options={
                'db_table': 'tipoproducto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomusuario', models.CharField(blank=True, db_column='nomUsuario', max_length=200, null=True)),
                ('tipousuario', models.CharField(blank=True, db_column='tipousuario', max_length=200, null=True)),
                ('apeusuario', models.CharField(blank=True, db_column='apeUsuario', max_length=200, null=True)),
                ('correousuario', models.CharField(blank=True, db_column='correoUsuario', max_length=100, null=True)),
                ('fechainscripcion', models.DateTimeField(blank=True, db_column='fechaInscripcion', null=True)),
                ('estado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idventa', models.IntegerField(db_column='idVenta', primary_key=True, serialize=False)),
                ('fechaventa', models.DateTimeField(db_column='fechaVenta')),
                ('importeventa', models.FloatField(db_column='importeVenta')),
                ('fechaentrega', models.DateTimeField(blank=True, db_column='fechaEntrega', null=True)),
                ('direccionentrega', models.CharField(blank=True, db_column='direccionEntrega', max_length=200, null=True)),
                ('observacionentrega', models.CharField(blank=True, db_column='observacionEntrega', max_length=200, null=True)),
                ('estadoentrega', models.IntegerField(blank=True, db_column='estadoEntrega', null=True)),
                ('observacionestadoentrega', models.CharField(blank=True, db_column='observacionEstadoEntrega', max_length=200, null=True)),
                ('idcliente', models.ForeignKey(blank=True, db_column='idCliente', null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Cliente')),
            ],
            options={
                'db_table': 'venta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VentaProducto',
            fields=[
                ('iddetalle', models.IntegerField(db_column='idDetalle', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField(db_column='Precio')),
                ('subtotal', models.IntegerField()),
                ('descuento', models.IntegerField(blank=True, null=True)),
                ('idprod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Producto')),
                ('idventa', models.ForeignKey(blank=True, db_column='idVenta', null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Venta')),
            ],
            options={
                'db_table': 'venta_producto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Valoracion',
            fields=[
                ('idvaloracion', models.IntegerField(db_column='id_Valoracion', primary_key=True, serialize=False)),
                ('puntage', models.IntegerField(blank=True, db_column='Puntage', null=True)),
                ('idprod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Producto')),
            ],
            options={
                'db_table': 'valoracion',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='idtallaproducto',
            field=models.ManyToManyField(to='servicios.Talla'),
        ),
        migrations.AddField(
            model_name='producto',
            name='idtipoproducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Tipoproducto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Usuario'),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('idpago', models.IntegerField(db_column='idPago', primary_key=True, serialize=False)),
                ('fechapago', models.DateTimeField(db_column='fechaPago')),
                ('importepago', models.FloatField(db_column='importePago')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('observacion', models.CharField(blank=True, max_length=200, null=True)),
                ('idtipopago', models.ForeignKey(blank=True, db_column='idTipoPago', null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Tipopago')),
                ('idventa', models.ForeignKey(blank=True, db_column='idVenta', null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Venta')),
            ],
            options={
                'db_table': 'pago',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Historialconsulta',
            fields=[
                ('idconsulta', models.IntegerField(db_column='idConsulta', primary_key=True, serialize=False)),
                ('fechaconsulta', models.DateField(blank=True, db_column='fechaConsulta', null=True)),
                ('horaconsulta', models.DateTimeField(blank=True, db_column='HoraConsulta', null=True)),
                ('nivelnavegacion', models.CharField(blank=True, db_column='NivelNavegacion', max_length=60, null=True)),
                ('idprod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Producto')),
            ],
            options={
                'db_table': 'historialconsulta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgfoto', models.ImageField(blank=True, upload_to='productos')),
                ('idprod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Producto')),
            ],
            options={
                'db_table': 'foto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('idcomentario', models.IntegerField(db_column='idComentario', primary_key=True, serialize=False)),
                ('comentario', models.CharField(db_column='Comentario', max_length=200)),
                ('idprod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Producto')),
            ],
            options={
                'db_table': 'comentario',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='idusuario',
            field=models.ForeignKey(blank=True, db_column='idUsuario', null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Usuario'),
        ),
        migrations.CreateModel(
            name='Carritocompras',
            fields=[
                ('idcarrito', models.IntegerField(db_column='idCarrito', primary_key=True, serialize=False)),
                ('fechacarrito', models.DateTimeField(blank=True, db_column='fechaCarrito', null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('preciototal', models.FloatField(blank=True, db_column='precioTotal', null=True)),
                ('FK_DetalleCarrito', models.ManyToManyField(to='servicios.Producto')),
            ],
            options={
                'db_table': 'carritocompras',
                'managed': True,
            },
        ),
    ]
