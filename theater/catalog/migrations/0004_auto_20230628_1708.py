# Generated by Django 3.2.12 on 2023-06-28 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_booking_status_remove_play_genre_play_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='contact',
            field=models.CharField(help_text='Введите номер телефона актера', max_length=200, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='date_of_birth',
            field=models.DateField(help_text='Введите дату рождения актера', verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(help_text='Введите имя актера', max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='surname',
            field=models.CharField(help_text='Введите фамилию актера', max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='amount',
            field=models.PositiveIntegerField(help_text='Введите кол-во бронируемых билетов', verbose_name='Кол-во билетов'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.play', verbose_name='Спектакль'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.BooleanField(default=False, help_text='Укажите, подтверждена ли бронь', verbose_name='Подтверждено'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='viewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.viewer', verbose_name='Зритель'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Введите название жанра (например, драма или комедия)', max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='play',
            name='datetime',
            field=models.DateTimeField(help_text='Введите дату и время', verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='play',
            name='director',
            field=models.CharField(help_text='Введите ФИ режиссера', max_length=200, verbose_name='Режиссер'),
        ),
        migrations.RemoveField(
            model_name='play',
            name='genre',
        ),
        migrations.AddField(
            model_name='play',
            name='genre',
            field=models.ManyToManyField(help_text='Выбери жанр', to='catalog.Genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='play',
            name='name',
            field=models.CharField(help_text='Введите название спектакля', max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='review',
            name='mark',
            field=models.PositiveIntegerField(help_text='Поставьте оценку спектаклю (от 1 до 10)', verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='review',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.play', verbose_name='Спектакль'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(help_text='Введите текст отзыва', verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='review',
            name='viewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.viewer', verbose_name='Зритель'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.play', verbose_name='Спектакль'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Введите стоимость билета', max_digits=8, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='seatkind',
            field=models.CharField(help_text='Введите название категории места', max_length=200, verbose_name='Категория места'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='seatnum',
            field=models.PositiveIntegerField(help_text='Введите номер места', verbose_name='Номер места'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.BooleanField(default=True, help_text='Укажите, доступен ли к продаже билет', verbose_name='Доступен (не продан)'),
        ),
        migrations.AlterField(
            model_name='viewer',
            name='contact',
            field=models.CharField(help_text='Введите номер телефона зрителя', max_length=200, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='viewer',
            name='name',
            field=models.CharField(help_text='Введите имя зрителя', max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='viewer',
            name='surname',
            field=models.CharField(help_text='Введите фамилию зрителя', max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='viewer',
            name='visits',
            field=models.PositiveIntegerField(default=0, help_text='Введите кол-во предыдущих посещений театра', verbose_name='Кол-во посещений'),
        ),
    ]
