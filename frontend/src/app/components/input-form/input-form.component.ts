import { Component, OnInit, EventEmitter, Output} from '@angular/core';
import { AbstractControl,FormControl ,FormGroup, Validators, ValidationErrors, ValidatorFn } from '@angular/forms';
import {RequestBody} from '../../models/request-body'
@Component({
  selector: 'app-input-form',
  templateUrl: './input-form.component.html',
  styleUrls: ['./input-form.component.css']
})
export class InputFormComponent implements OnInit {
  input_form !:FormGroup;
  at_least_one:boolean = false;

  @Output() onRequestChange = new EventEmitter<RequestBody>();
  @Output() onSubmit = new EventEmitter();
  ngOnInit(): void {
    this.input_form = new FormGroup({
      width: new FormControl("", createValidIntegerValidator()),
      height: new FormControl("", createValidIntegerValidator()),
      x1: new FormControl("",createValidFloatValidator()),
      x2: new FormControl("",createValidFloatValidator()),
      x3: new FormControl("",createValidFloatValidator()),
      x4: new FormControl("",createValidFloatValidator()),
      y1: new FormControl("",createValidFloatValidator()),
      y2: new FormControl("",[createValidFloatValidator()]),
      y3: new FormControl("",[createValidFloatValidator()]),
      y4: new FormControl("",[createValidFloatValidator()]),
    });
  }

  add() {
    const form_controls = this.input_form.controls;
    const dimensions = [parseFloat(form_controls["width"].value), parseFloat(form_controls["height"].value)];
    const corners = [
      [parseFloat(form_controls["x1"].value), parseFloat(form_controls["y1"].value)],
      [parseFloat(form_controls["x2"].value), parseFloat(form_controls["y2"].value)],
      [parseFloat(form_controls["x3"].value), parseFloat(form_controls["y3"].value)],
      [parseFloat(form_controls["x4"].value), parseFloat(form_controls["y4"].value)],
    ]
    const req_body = new RequestBody(dimensions, corners);
    this.at_least_one = true;
    this.onRequestChange.emit(req_body);
  }

  submit() {
    this.at_least_one = false;
    this.onSubmit.emit();
  }



}


export function createValidIntegerValidator(): ValidatorFn {
    return (control:AbstractControl) : ValidationErrors | null => {
        const value = control.value;
        if(!value){
          return {"error":"Must be a Postive Integer"};
        }
        const result = value.match(/^[0-9]+.?[0]*/);
        if(!result || value.length != result[0].length){
          return {"error":"Must be a Postive Integer"};
        }
        return null
    }
}

export function createValidFloatValidator(): ValidatorFn {
    return (control:AbstractControl) : ValidationErrors | null => {
        const value = control.value;
        if(!value){
          return {"error":"Must be a Positive Float"};
        }
        const result = value.match(/^[0-9]+.?[0-9]*/)
        if(!result || value.length != result[0].length){
          console.log("error")
          return {"error":"Must be a Positive Float"};
        }
        return null
    }
}
