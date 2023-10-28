import { Component, Input, inject } from '@angular/core';
import { Router } from '@angular/router';
import { GetFormsService } from '../get-forms.service';
import { FormList } from '../formList';

@Component({
  selector: 'app-journal-entry',
  templateUrl: './journal-entry.component.html',
  styleUrls: ['./journal-entry.component.css'],
  standalone: true
})

export class JournalEntryComponent {
  getFormservice: GetFormsService = inject(GetFormsService);
  formList!: FormList;
  constructor(private router : Router) {
    this.getFormservice.getForm().subscribe((response: any) => {
      const jsonString = JSON.stringify(response);
      this.formList = JSON.parse(jsonString);
      console.log(this.formList);
    });
  }
}