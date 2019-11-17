package com.deepconnect.beatmanagement;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class MainActivity extends AppCompatActivity {

  private Button login_btn, register_btn;

  private EditText ET_email , ET_pass;

    private FirebaseAuth mAuth;

//    @Override
//    public void onStart() {
//        super.onStart();
//        // Check if user is signed in (non-null) and update UI accordingly.
//        FirebaseUser currentUser = mAuth.getCurrentUser();
//        Intent intent = new Intent(MainActivity.this , ListActivity.class);
//        startActivity(intent);
//    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Initialize Firebase Auth
        mAuth = FirebaseAuth.getInstance();

       FindViews();

       register_btn.setOnClickListener(new View.OnClickListener() {
           @Override
           public void onClick(View v) {
               UserRegister();
           }
       });

       login_btn.setOnClickListener(new View.OnClickListener() {
           @Override
           public void onClick(View v) {
               UserLogin();
           }
       });

    }

    private void FindViews() {
        ET_email = findViewById(R.id.user_email);
        ET_pass = findViewById(R.id.user_password);
        login_btn = findViewById(R.id.Login_btn);
        register_btn = findViewById(R.id.signup_btn);
    }

    private void UserRegister() {
         String email = ET_email.getText().toString().trim();
         String pass = ET_pass.getText().toString().trim();

        mAuth.createUserWithEmailAndPassword(email, pass)
                .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if (task.isSuccessful()) {
                            Intent intent = new Intent(MainActivity.this , ListActivity.class);
                            startActivity(intent);

                        } else {
                            Toast.makeText(MainActivity.this , "problem in registering", Toast.LENGTH_SHORT).show();

                        }

                    }
                });
    }

    private void UserLogin()
    {
        String email = ET_email.getText().toString().trim();
        String pass = ET_pass.getText().toString().trim();
        mAuth.signInWithEmailAndPassword(email, pass)
                .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if (task.isSuccessful()) {
                            Intent intent = new Intent(MainActivity.this , TakePictureActivity.class);
                            startActivity(intent);
                        } else {
                            Toast.makeText(MainActivity.this , "Please verify details", Toast.LENGTH_SHORT).show();

                        }


                    }
                });
    }
}

