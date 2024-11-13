#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_7_clicked()
{
    QString fileName = QFileDialog::getOpenFileName(this,
        tr("Datei öffnen"),
        "",
        tr("Alle Dateien (*);;Textdateien (*.txt)")
        );
}

