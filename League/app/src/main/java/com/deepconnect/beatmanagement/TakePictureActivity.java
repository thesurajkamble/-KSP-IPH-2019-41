package com.deepconnect.beatmanagement;

import android.app.ProgressDialog;
import android.content.ContentResolver;
import android.content.Intent;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.provider.MediaStore;
import android.view.View;
import android.webkit.MimeTypeMap;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.Toast;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.OnProgressListener;
import com.google.firebase.storage.StorageReference;
import com.google.firebase.storage.StorageTask;
import com.google.firebase.storage.UploadTask;

import java.io.IOException;
import java.util.Objects;

public class TakePictureActivity extends AppCompatActivity {

    private StorageReference mStorageRef;

    ImageView IV_image;


    Button camera_btn;
    Button Upload_btn;
    private static final int CAMERA_REQUEST_CODE = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_take_picture);
//        mProgressBar = new ProgressDialog(this);
        mStorageRef = FirebaseStorage.getInstance().getReference();

        camera_btn = findViewById(R.id.camera_btn);
        IV_image = findViewById(R.id.IV_image);

        camera_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(TakePictureActivity.this, "click on", Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
//                intent.setType("image/*");
                Toast.makeText(TakePictureActivity.this, "click off", Toast.LENGTH_SHORT).show();
                startActivityForResult(intent, CAMERA_REQUEST_CODE);
                finish();
            }
        });

    }


}
