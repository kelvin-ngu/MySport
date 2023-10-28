import { Component, Input } from '@angular/core';
import { FormList } from '../formList';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-entry',
  templateUrl: './entry.component.html',
  styleUrls: ['./entry.component.css'],
  imports: [CommonModule],
  standalone: true
})
export class EntryComponent {
    @Input() formList!: FormList;
}

