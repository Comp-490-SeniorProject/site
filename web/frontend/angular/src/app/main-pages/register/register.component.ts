import {Component, OnInit} from "@angular/core"
import {FormGroup} from "@angular/forms"
import {Validators} from "@angular/forms"
import {FormBuilder} from "@angular/forms"
import {Router} from "@angular/router"
import {AuthService} from "src/app/auth/auth.service"

@Component({
    selector: "app-register",
    templateUrl: "./register.component.html",
    styleUrls: ["./register.component.scss"],
})
export class RegisterComponent implements OnInit {
    constructor(
        private authService: AuthService,
        private router: Router,
        private formBuilder: FormBuilder
    ) {}

    authForm!: FormGroup
    isSubmitted = false

    ngOnInit() {
        this.authForm = this.formBuilder.group({
            username: ["", Validators.required],
            email: [""],
            password: ["", Validators.required],
            password_confirm: ["", Validators.required],
        })
    }

    get formControls() {
        return this.authForm.controls
    }

    usernameStatus: any
    passwordStatus: any
    password_confirmStatus: any
    emailStatus: any
    status: any
    register() {
        this.isSubmitted = true
        if (this.authForm.invalid) {
            return
        }
        this.authService.register(this.authForm.value).subscribe(
            (res: any) => {
                this.status = "User Created..!"
                this.usernameStatus = ""
                this.passwordStatus = ""
                this.password_confirmStatus = ""
                this.emailStatus = ""
                setTimeout(() => {
                    this.router.navigateByUrl("homepage")
                }, 3000)
            },
            (error) => {
                this.usernameStatus = error.error["username"]
                this.passwordStatus = error.error["password"]
                this.password_confirmStatus = error.error["password_confirm"]
                this.emailStatus = error.error["email"]
            }
        )
    }
}
