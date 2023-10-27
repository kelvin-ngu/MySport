import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';

import { RouterModule } from '@angular/router';
import { MygameComponent } from './mygame/mygame.component';
import { JournalEntryComponent } from './journal-entry/journal-entry.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    MygameComponent,
    JournalEntryComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot([
      {path: '', component: HomeComponent},
      {path: 'mygame', component: MygameComponent},
    ]),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
