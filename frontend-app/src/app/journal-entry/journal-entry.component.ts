import { Component, Input, inject } from '@angular/core';
import { Router } from '@angular/router';
import { EntryComponent } from '../entry/entry.component';
import { GetFormService } from '../get-forms.service';
import { FormList } from '../formList';

@Component({
  selector: 'app-journal-entry',
  templateUrl: './journal-entry.component.html',
  styleUrls: ['./journal-entry.component.css'],
  standalone: true,
  imports: [EntryComponent]
})

export class JournalEntryComponent {
  getFormService: GetFormService = inject(GetFormService)
  formList!: FormList
  constructor(private router : Router) {
    this.getFormService.getForms().subscribe((response) => {
      const jsonString = JSON.stringify(response);
      this.formList = JSON.parse(jsonString);
      console.log(this.formList);
     });
  }

  navigateTo(route: string) {
    this.router.navigate([route]);
  }
}